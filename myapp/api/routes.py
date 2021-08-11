# api
from flask import Blueprint

api = Blueprint('api', __name__, url_defaults='/api')

@api.route('/getdata')
def getdata():
    return {'key' : 'value'}