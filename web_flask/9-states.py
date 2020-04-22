#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    states = storage.all("State")
    if id:
        states = states.get('State.{}'.format(id), None)
    return render_template('9-states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
