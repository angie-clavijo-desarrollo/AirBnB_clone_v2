#!/usr/bin/python3
""" Flask hello world and other path and specify port and host
    And render and file html, one path specify"""
from flask import Flask, render_template

app = Flask(__name__)


app.route('/states_list', strict_slashes=False)


def path_states(State="States"):
    return render_template('7-states_list.html', State=State)


if __name__ == '__main__':
    app.run(debug=True)
