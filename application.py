import os
import sys
import json

import flask
from flask import request, Response

# Create the Flask app
app = flask.Flask(__name__)

back_end = os.environ['FIBONACCI_BE_ADDRESS']

@app.route('/')
def welcome():
    return flask.render_template('index.html', back_end = back_end)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("80"))
