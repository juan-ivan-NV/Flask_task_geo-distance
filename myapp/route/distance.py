# flask
from flask import Blueprint, render_template, request, flash, current_app

# python
import urllib, json, logging, math
import mpu

# keys
import config

mkad_route = Blueprint("mkad_route", __name__, 
                       static_folder="static", template_folder = "templates")

# Yandex variables

api_key = config.API_KEY
"""https://geocode-maps.yandex.ru/1.x/?apikey=ваш 
API-ключ&geocode=Москва,+Тверская+улица,+дом+7"""
api_url = ("https://geocode-maps.yandex.ru/1.x/?apikey={}" +
        "&format=json&geocode={}&lang=en-US")

def get_distance(lat1: float, lng1: float,
                lat2: float, lng2: float):

        """function to calculate distance"""

        return mpu.haversine_distance((lat1, lng1), (lat2, lng2))

def api_request(address_request: str):

        """Function to validate if the request (address) 
        is valid or not"""

        api_response = urllib.request.urlopen(api_url.format(
                api_key, address_request)).read()
        api_json = json.loads(api_response)
        found_data = (
            api_json["response"]["GeoObjectCollection"]
            ["metaDataProperty"]["GeocoderResponseMetaData"]["found"]
        )

        if found_data == "0":
                api_json = None
                return False, api_json
        else: 
                return True, api_json


def json_req_data(json_api_data: dict):
        
        """ This functions extracts usefull data from the 
        api response dictionary"""

        MKAD = [55.898947, 37.632206]

        position = (json_api_data["response"]["GeoObjectCollection"]
                        ["featureMember"][0]["GeoObject"]["Point"]["pos"]).split(" ")

        lat = float(position[0])
        long = float(position[1])

        json_dictionary = json.dumps([
        (json_api_data["response"]["GeoObjectCollection"]["featureMember"]
            [0]["GeoObject"]["name"])])

        distance = get_distance(lat, long, MKAD[0], MKAD[1])

        return json_dictionary, distance

def address_request():

        """Function to order the values to be showed in the html template"""

        address = None
        distance = None
        json_message = {}
        validation = False

        if request.method == 'POST':
                address = request.form['address']
                
                if address_request == "":
                        flash(f"Try with a valid location")
                        return json_message, address, distance, validation
                else: 
                        address = address.replace(" ", "+")
                        validation, api_data = api_request(address)
                        
                        if validation is False:
                                flash(f"Validation false, noresults found")
                                return json_message, address, distance, validation 
                        else:
                                flash (f"address entered {address}", "info")
                                json_message, distance = json_req_data(api_data)
                                return json_message, address, distance, validation
                
        return json_message, address, distance, validation


def logging_request(request_json: dict, user_post_query: str,
                    distance: float, valid_request: bool):

        """Function to save info in the log data file"""

        logging.basicConfig(
            filename='history.log',
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(threadName)s : %(message)s'
        )
        if valid_request is True:
                current_app.logger.info(f"JSON {request_json}")
                current_app.logger.info(f"Searched for {user_post_query}")
                current_app.logger.info(f"Distance between points is: {distance} Km")
        else:
                current_app.logger.info("Invalid request")

# decorators for the blueprints
@mkad_route.route("/", methods=['POST', 'GET'])
@mkad_route.route("/home", methods=['POST', 'GET'])


def route_search():
        
        """function to call the other functions to process the direction request
        and return the data to the html template"""

        result_json, address, distance, valid_request = address_request()
        logging_request(result_json, address, distance, valid_request)
        
        return render_template('search.html',
        address = address,
        api_key = config.API_KEY,
        result_json = result_json
        )
