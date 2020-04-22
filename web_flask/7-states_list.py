#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    /states_list: display a HTML page: (inside the tag BODY)
    """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
