from flask import Flask, redirect

from route.distance import mkad_route
import config 

main_app = Flask(__name__)

# blieprint
main_app.register_blueprint(mkad_route, url_prefix="/route")
# flask secret access key
main_app.secret_key = config.SECRET_KEY

@main_app.route("/")

def index():
    
    return redirect('/route')

if __name__ == "__main__":
    main_app.run(debug=True)

