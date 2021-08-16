from flask import Blueprint, jsonify, current_app
import requests
from math import sin, cos, sqrt, atan2, radians

import mpu

#MKAD_CENTER = "37.6222,55.7518"
MKAD_CENTER = [37.6222,55.7518]
MKAD_RADIUS = "0.2152,0.16"
API_KEY = "XXXXXXXX"
EARTH_RADIUS = 6373.0

# to define blueprint

yandex_dist = Blueprint('yandex_dist', __name__, url_prefix='/yandex')

p1, p2, p2_in_MKAD = '','',''

@yandex_dist.route("/", methods=["GET"])
def home():
    return """
    <table>
        <tr>
            <td>/(address)</td>
            <td>for calculate address from MKAD</td>
        </tr>
    </table>
    """



def calculate_distance_1(p1, p2):

    return mpu.haversine_distance((p1[0], p1[1]), (p2[0], p2[1]))


def address_coordinates(address, checkMKAD = False):

    print(address)

    url = ('https://geocode-maps.yandex.ru/1.x/?' + 'apikey=' + API_KEY
            + '&geocode=' + address + '&format=json&results=1&lang=en-US'
            )

    if checkMKAD :
        url += ('&ll='+ "37.6222,55.7518" + '&spn='+ MKAD_RADIUS + '&rspn=1' 
            )

    response = requests.get(url).json()

    print(response)

    try: 
        position = response['response']['GeoObjectCollection']['featureMember']\
                   [0]['GeoObject']['Point']['pos']
        place = response["response"]["GeoObjectCollection"]["featureMember"]\
                   [0]["GeoObject"]["name"]
        position = position.split(' ')
        position = list(map(float, position))
        point2 = [position[1], position[0]] 
        print(point2, place)
        return point2, place

    except:
        return [0,0]


def get_coordintes(coords):

    global p1, p2, address2, p2_in_MKAD
    p1 = MKAD_CENTER
    p2, address2 = address_coordinates(coords)
    p2_in_MKAD = address_coordinates(coords, checkMKAD = True)[0]


@yandex_dist.route("/<address>")
def logging_distances(address):
   
    introduced_coords = address

    get_coordintes(introduced_coords)

    if p2 == p2_in_MKAD:
        log1 = str(p2) + ' is inside MKAD, distance not calculated'
        current_app.logger.info(log1)
        print(log1)
        return jsonify({'status':200, 'message':'Success',
                        'data':{'address1' : 'MKAD', 'coordinate1': p1,
                                'address2': address2, 'coordinate2': p2,
                                'distance': 0, 'unit': 'km', 'info': log1
                    }})

    else:
        
        distance = calculate_distance_1(p1, p2)
        log1 = 'address 1 is MKAD, address 2 is ' + str(p2[0]) \
                + str(p2[1]) + 'address: ' + address2
        current_app.logger.info(log1)
        return jsonify({'status':200, 'message':'Success',
                 'data':{'address1' : 'MKAD', 'coordinate1': p1,
                         'address2': address2, 'coordinate2': p2,
                         'distance': distance, 'unit': 'km', 'info': ''
            }})    
