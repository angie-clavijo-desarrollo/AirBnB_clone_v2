#!/usr/bin/python3
""" Flask hello world and other path and specify port and host"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb')
def path_hbnbn():
    return "HBNB"


@app.route('/c/<text>')
def path_c(text="value"):
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(debug=True)
