#!/usr/bin/python3
""" Flask one path and specify port and host
    And render and file html, to extract all data """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<string:id>', strict_slashes=False)
def list_cities_states(id=None):
    """list_cities_states - function"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template(
        '9-states.html', states=states, cities=cities, id=id)


@app.teardown_appcontext
def remove_session(self):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True)
