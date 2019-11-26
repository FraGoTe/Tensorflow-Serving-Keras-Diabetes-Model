import base64
import json
from io import BytesIO

#import numpy as np
import requests
from flask import Flask, request, jsonify

from flask_cors import CORS

app = Flask(__name__)

# Uncomment this line if you are making a Cross domain request
cors = CORS(app, resources={r"/diabetes/predict/": {"origins": "*"}})


# Testing URL
@app.route('/hello/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello, World!'


@app.route('/diabetes/predict/', methods=['POST'])
def diabetes_classifier():
    # Making POST request
    r = requests.post('http://francis-gonzales.info:8501/v1/models/diabetes:predict', json=json.loads(request.data))

    # Decoding results from TensorFlow Serving server
    pred = json.loads(r.content.decode('utf-8'))

    # Returning JSON response to the frontend
    return jsonify(pred)


# export FLASK_ENV=development && flask run --port 8080 --host 0.0.0.0 >> flask_error_log.txt 2>&1 &
# nohup  flask run --port 8080 --host 0.0.0.0 >> flask_error_log.txt 2>&1 &