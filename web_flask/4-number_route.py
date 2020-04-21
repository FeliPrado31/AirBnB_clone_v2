#!/usr/bin/python3
# Write a script that starts a Flask web application:

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hi():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """display “n is a number” only if n is an integer
    """
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
