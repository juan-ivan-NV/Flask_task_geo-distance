# flask imports
import requests
from math import sin, cos, sqrt, atan2, radians

import mpu

#MKAD_CENTER = "37.6222,55.7518"
MKAD_CENTER = [37.6222, 55.7518]
MKAD_RADIUS = "0.2152,0.16"
API_KEY = "xxxxx"
EARTH_RADIUS = 6373.0

# to define blueprint

p1, p2, is_p2_in_MKAD = '','',''

#p1 = [0,0]
#p1[0] = float(input("type lat (should be float): "))
#p1[1] = float(input("type lng (should be float): "))


def calculate_distance_1(p1, p2):

    return mpu.haversine_distance((p1[0], p1[1]), 
                                  (MKAD_CENTER[0], MKAD_CENTER[1]))


def address_coordinates(address):

    print(address)
    """url = ("https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}" +
        "&geocode=55.54560447733747,37.59266627650848&format=json&results=1&lang=en-US")"""

    url = ('https://geocode-maps.yandex.ru/1.x/?' + 'apikey=' + API_KEY
                + '&geocode=' + address
                + '&format=' + 'json'
                + '&results=1'
                + '&lang=en-US'
            )


    response = requests.get(url).json()

    print(response)

    try: 
        position = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        position = position.split(' ')
        position = list(map(float, position))
        point2 = [position[1], position[0]] 
        print(point2)
        return point2 

    except:
        return [0,0]

    return x

address = "55.54560447733747,37.59266627650848"

p2 = address_coordinates(address)

print(calculate_distance_1(MKAD_CENTER, p2))