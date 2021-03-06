#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    users = storage.all("User")
    return render_template('100-hbnb.html', states=states, amenities=amenities,
                           places=places, users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
