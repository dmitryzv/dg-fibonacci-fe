import os
import sys
import json

import flask
from flask import request, Response

# Create the Flask app
app = flask.Flask(__name__)

@app.route('/')
def welcome():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("80"))
