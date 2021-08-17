# TEST TASK: Flask-Yandex-Find-Distance

## Description

Develop a Flask Blueprint to find the distance from the Moscow Ring Road to the specified address. The address is passed to the application in an HTTP request, if the specified address is located inside the MKAD, the distance does not need to be calculated. Add the result to the .log file.


## Requirements:

* The address is transmitted via an HTTP request
* The functions and algorithms used are provided with informative comments
* The tests are arranged in a separate file
* Documentation in the form of readme.md the file contains instructions for using the application
* PEP8 code compliance and use of type annotations


## Requirements for tools:

1. Python version no older than 3.8
2. Source code must be published on Github/Gitlab/Bitbucket
3. It will be a plus to create a Docker container with the application


### Instructions

Requierements:

    Flask
    mpu
    request
    virtualenv
    requests

For Linux:

Clone the repo:

<pre>git clone https://github.com/juan-ivan-NV/Flask_task_geo-distance.git</pre>

Activate the virtual enviroment

<pre>source my_env_project/bin/activate</pre>

Install Flask

<pre>pip install flask</pre>

Install mpu

<pre>pip install mpu</pre>

Execute the app

<pre>python app.py</pre>


## Usage

* In your browser type ...

<pre>http://localhost:5000/</pre>

You will she the app "homepage".

* To go to the Blueprint endpoint type on you browser...

<pre>http://localhost:5000/yandex</pre>

You will se the page and a message from that endpoint.

* To look for a location type a location, for example ...

<pre>http://localhost:5000/yandex/Kyev</pre>

You should see something like this.

<pre>{
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
            </pre>
