# flask
from flask import Blueprint, render_template, request, flash, current_app

# python
import urllib, json, logging, math
import mpu

# keys
import config

route = Blueprint("route", __name__, template_folder = "templates")

# Yandex variables

api_key = config.API_KEY
"""https://geocode-maps.yandex.ru/1.x/?apikey=ваш 
API-ключ&geocode=Москва,+Тверская+улица,+дом+7"""
api_url = ("https://geocode-maps.yandex.ru/1.x/?apikey={}" +
        "&format=json&geocode={}&lang=en-US")

def get_distance(lat1: float, lng1: float,
                lat2: float, lng2: float):

        """function to calculate distance"""

        return mpu.haversine_distance(lat1, lng1), (lat2, lng2)).km

def api_request(address_request: str):

        """Function to validate if the request (address) 
        is valid or not"""

        api_response = urllib.request.urlopen(api_url.format(
                api_key, address_request)).read()
        api_json = json.loads(api_response)
        found_data = (api_json["response"]["GeoObjectCollection"]
                      ["metaDataProperty"]["geocoderResponseMetaData"]["found"]
        )

        if found_data == "0":
                api_json = None
                return False, api_json
        else: 
                return True, api_json


def json_req_data(json_api_data: dict):
        
        """ This functions extracts usefull data from the 
        api response dictionary"""

        

def address_request():

        address_request = None
        
        pass

def logging_request():

        pass

def route_search():
        pass
