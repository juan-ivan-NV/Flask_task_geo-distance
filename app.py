from flask import Flask
from distance.yandex_distance import yandex_dist
import logging

app = Flask(__name__)

app.register_blueprint(yandex_dist)

@app.route("/")

def main_app():
    return """
    <h2>Blueprint to measure distance from MKAD to another coordinate<h2>

    <table>
    <tr>
        <td>/yandex</td>
        <td>for using Yandex API</td>
    </tr>
    </table>
    """

logging.basicConfig(filename='record.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)