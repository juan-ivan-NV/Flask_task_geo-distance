from flask import Flask, redirect

#from route import redir
# import config 

main_app = Flask(__name__)

# blieprint
main_app.register_blueprint(route, url_prefix="")