import json

import pytest

from app import app as flask_app

""" To load the cases"""
@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


"""Cases or tests"""
def test1_outside_MKAD(client):
    #Passing kiev as address

    response = client.get("/yandex/Kyev")
    #response = logging_distances ()
    expected = {
            "data": {
                "address1": "MKAD", 
                "address2": "Kyiv", 
                "coordinate1": [37.6222, 55.7518], 
                "coordinate2": [50.450441, 30.52355], 
                "distance": 755.5756107294386, 
                "info": "", 
                "unit": "km"}, 
            "message": "Success", 
            "status": 200
            }

    assert expected == json.loads(response.get_data(as_text=True))


def test2_outside_MKAD(client):
    #Passing Riga as address

    response = client.get("/yandex/Riga")
    expected = {
            "data": {
                "address1": "MKAD", 
                "address2": "Riga", 
                "coordinate1": [37.6222, 55.7518], 
                "coordinate2": [56.946845, 24.106075], 
                "distance": 841.908557563649, 
                "info": "", 
                "unit": "km"
            }, 
            "message": "Success", 
            "status": 200
            }

    assert expected == json.loads(response.get_data(as_text=True))


def test3_inside_MKAD(client):
    #Passing Savyolovskaya as address

    response = client.get("/yandex/Savyolovskaya")
    expected = {
            "data": {
                "address1": "MKAD", 
                "address2": "Savyolovskaya metro station", 
                "coordinate1": [37.6222, 55.7518], 
                "coordinate2": [55.792807, 37.586122], 
                "distance": 0, 
                "info": "[55.792807, 37.586122] is inside Moscow Ring Road, so distance is not calculated", 
                "unit": "km"}, 
            "message": "Success", 
            "status": 200
            }

    assert expected == json.loads(response.get_data(as_text=True))


def test4_inside_MKAD(client):
    #Passing Shabolovskaya as address

    response = client.get("/yandex/Shabolovskaya")
    expected = {
            "data": {
                "address1": "MKAD", 
                "address2": "Shabolovskaya metro station", 
                "coordinate1": [37.6222, 55.7518], 
                "coordinate2": [55.718821, 37.607933], 
                "distance": 0, 
                "info": "[55.718821, 37.607933] is inside Moscow Ring Road, so distance is not calculated", 
                "unit": "km"
                }, 
            "message": "Success", 
            "status": 200
            }

    assert expected == json.loads(response.get_data(as_text=True))


def test5_invalid_input(client):
    #Passing a non-existent place
    
    response = client.get("/yandex/wherethestreetshavenoname")
    expected = {
            "info": """Requested address No Name Key not found \u00af\\_(\u30c4)_/\u00af""", 
            "message": "Bad Request", 
            "status": 400
            }

    assert expected == json.loads(response.get_data(as_text=True))


