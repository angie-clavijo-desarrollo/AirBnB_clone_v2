#!/usr/bin/python3
""" Flask one path and specify port and host
    And render and file html, to """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def path_states():
    state = storage.all(State).values()
    return render_template('7-states_list.html', states=state)


@app.teardown_appcontext
def remove_session(self):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True)
