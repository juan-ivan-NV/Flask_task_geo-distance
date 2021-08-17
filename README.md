
example1: http://localhost:5000/yandex/(37.902943279027895,55.41663012089028)
example2: http://localhost:5000/yandex/Kiev

Activate env: $ 


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

In your browser type

<pre>http://localhost:5000/</pre>

On screen

<h2>Blueprint to measure distance from MKAD to another coordinate<h2>

    <table>
    <tr>
        <td>/yandex</td>
        <td>to use Yandex API</td>
    </tr>
    <tr>
        <td>example:</td>
        <td>http://localhost:5000/yandex</td>
    </tr>
    </table>
