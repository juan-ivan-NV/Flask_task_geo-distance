# flask imports
import requests
from math import sin, cos, sqrt, atan2, radians

import mpu

#MKAD_CENTER = "37.6222,55.7518"
MKAD_CENTER = [37.6222, 55.7518]
MKAD_RADIUS = "0.2152,0.16"
API_KEY = '60a38614-54fe-4fb4-a9fe-355b8f32c2cd'
EARTH_RADIUS = 6373.0

# to define blueprint

p1, p2, is_p2_in_MKAD = '','',''

p1 = [0,0]
p1[0] = float(input("type lat (should be float): "))
p1[1] = float(input("type lng (should be float): "))


def calculate_distance_1(p1, p2):

    return mpu.haversine_distance((p1[0], p1[1]), 
                                  (MKAD_CENTER[0], MKAD_CENTER[1]))



def calculate_distance_2(p1, p2):
    # Because Yandex API doesn't have calculate distance method
    # Source code from https://www.kite.com/python/answers/how-to-find-the-distance-between-two-lat-long-coordinates-in-python

    point1 = p1
    point2 = p2

    latitude = [radians(point1[0]), radians(point2[0])]
    longitude = [radians(point1[1]), radians(point2[1])]
    distance_latitude = latitude[0] - latitude[1]
    distance_logitude = longitude[0] - longitude[1]

    a = sin(distance_latitude / 2)**2 + cos(latitude[0]) * cos(latitude[1]) * sin(distance_logitude / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = EARTH_RADIUS * c

    return distance

print(calculate_distance_1(p1, MKAD_CENTER))
print(calculate_distance_2(p1, MKAD_CENTER))