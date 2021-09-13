#!/usr/bin/python3
""" Flask one path and specify port and host
    And render and file html, to extrac all data """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def path_cities_state():
    states = storage.all(State).values()
    cities = storage.all(City).values()

    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


@app.teardown_appcontext
def remove_session(self):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True)
