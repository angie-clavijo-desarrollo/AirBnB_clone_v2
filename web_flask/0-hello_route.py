#!/usr/bin/python3
""" Flask hello world and specify port and host"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
