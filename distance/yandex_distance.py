from flask import Blueprint, jsonify, current_app
import requests
import mpu

import config

MKAD_CENTER = [37.6222,55.7518]
MKAD_RADIUS = "0.2152,0.16"
API_KEY = config.API_KEY 
EARTH_RADIUS = 6373.0


yandex_dist = Blueprint('yandex_dist', __name__, url_prefix='/yandex')

p1, p2, p2_in_MKAD = '','',''

@yandex_dist.route("/", methods=["GET"])
def home():
    return """
    <h4>This Blueprint is to find the distance from the Moscow Ring Road to the 
    specified address. The address is passed to the application in an HTTP request, 
    if the specified address is located inside the MKAD, 
    the distance will not be calculated.<h4>

    <table>
        <tr>
            <td>/(address)</td>
            <td>to calculate address from MKAD</td>
        </tr>
        <tr>
            <td>example:</td>
            <td>http://localhost:5000/yandex/Kiev</td>
        </tr>
    </table>
    """


def calculate_distance_1(p1, p2):
    """
    Function to calculate the disctance.
    Input: p1 & p2, both are coordinates
    output: distance, is km between p1 and p2
    """

    return mpu.haversine_distance((p1[1], p1[0]), (p2[0], p2[1]))


def address_coordinates(address, checkMKAD = False):
    """
    Method to get the coordinates of the given address from Yandex API
    If address is within the MKAD zone coordinates will be the same as MKAD
    Input: address, name of a place
    Output: coordinates, lat, lng
    """

    url = ('https://geocode-maps.yandex.ru/1.x/?apikey=' + API_KEY
            + '&geocode=' + address + '&format=json&results=1&lang=en-US'
            )

    if checkMKAD :
        url += ('&ll='+ "37.6222,55.7518" + '&spn='+ MKAD_RADIUS + '&rspn=1' 
            )

    response = requests.get(url).json()

    try: 
        position = response['response']['GeoObjectCollection']['featureMember']\
                   [0]['GeoObject']['Point']['pos']
        address2 = response["response"]["GeoObjectCollection"]["featureMember"]\
                        [0]["GeoObject"]["name"]
        position = position.split(' ')
        position = list(map(float, position))
        point2 = [position[1], position[0]] 
        #print(point2, address2)
        return point2, address2

    except:
        return [[0,0],address]


def get_coordintes(address):
    """
    Method to get all coordinates and 
    redefine the following variables as globals
    Input: address, name of a place
    Output: None
    """
    
    global p1, p2, address2, p2_in_MKAD
    p1 = MKAD_CENTER
    p2, address2 = address_coordinates(address)
    p2_in_MKAD = address_coordinates(address, checkMKAD = True)[0]


@yandex_dist.route("/<address>")
def logging_distances(address):
    """
    Method to return logs, distance and address
    Input: address, Place is passed through the decorator above
    Output: json dictionaries with the data from the given address
    """

    get_coordintes(address)

    if p2 == [0,0] or p2 == [24.692661, -81.326369]:
       log1 = 'Requested address ' + address2 + ' not found ¯\_(ツ)_/¯'
       current_app.logger.error(log1)
       return jsonify({'status':400, 'message': 'Bad Request', 'info':log1})

    elif p2 == p2_in_MKAD:
        log1 = str(p2) + ' is inside Moscow Ring Road, so distance is not calculated'
        current_app.logger.info(log1)
        print(log1)
        return jsonify({'status':200, 'message':'Success',
                        'data':{'address1' : 'MKAD', 'coordinate1': p1,
                                'address2': address2, 'coordinate2': p2,
                                'distance': 0, 'unit': 'km', 'info': log1
                    }})

    else:
        distance = calculate_distance_1(p1, p2)
        log1 = 'Main address is MKAD, address 2 is ' \
                + " ".join([str(i) for i in p2]) + 'address: ' \
                + address2 + ' ,calculated distance = ' + str(distance)
        current_app.logger.info(log1)
        return jsonify({'status':200, 'message':'Success',
                 'data':{'address1' : 'MKAD', 'coordinate1': p1,
                         'address2': address2, 'coordinate2': p2,
                         'distance': distance, 'unit': 'km', 'info': ''
            }})    
