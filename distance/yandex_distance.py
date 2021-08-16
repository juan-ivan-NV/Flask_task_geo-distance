# flask imports
import requests
from math import sin, cos, sqrt, atan2, radians

import mpu

#MKAD_CENTER = "37.6222,55.7518"
MKAD_CENTER = [37.6222,55.7518]
MKAD_RADIUS = "0.2152,0.16"
API_KEY = "xxxxx"
EARTH_RADIUS = 6373.0

# to define blueprint

p1, p2, p2_in_MKAD = '','',''


def calculate_distance_1(p1, p2):

    """Function to calculate the distance between two coordinates
    inputs 
    p* = list of latitude and longitude"""

    return mpu.haversine_distance((p1[0], p1[1]), 
                                  (p2[0], p2[1]))


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
        position = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        position = position.split(' ')
        position = list(map(float, position))
        point2 = [position[0], position[1]] 
        print(point2)
        return point2 

    except:
        return [0,0]

    return x

def get_coordintes(address):

    global p1, p2, p2_in_MKAD
    p1 = MKAD_CENTER
    p2 = address_coordinates(address)
    p2_in_MKAD = address_coordinates(address, checkMKAD = True)

def logging_distances(address):

    #if p2 == [0,0]:
    #    log = '------ 'p2 + ' not found------'
    #    current_app.logger.error(log)
    #    return jsonify({'status':400, 'message':'Bad Request', 'data':log})
    
    if p2 == p2_in_MKAD:
        log = p2 + ' is inside MKAD, distance not calculated'
        #current_app.logger.info(log)
        print(log)
        return jsonify({'status':200, 'message':'Success',
                        'data':{'address1' : 'MKAD', 'coordinate1': point1,
                                'address2': address2, 'coordinate2': point2,
                                'distance': 0, 'unit': unit, 'info': log
                    }})
            



address = "37.522257143027474,55.77884116736447"

p2 = address_coordinates(address)

print(calculate_distance_1(MKAD_CENTER, p2))