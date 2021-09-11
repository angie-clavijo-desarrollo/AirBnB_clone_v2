#!/usr/bin/python3
""" Flask hello world and other path and specify port and host
    And render and file html, one path specify"""
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def path_python(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def path_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def path_number_temaple(n):
    return "Number: {}".format(n)
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
