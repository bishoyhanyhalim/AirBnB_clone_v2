#!/usr/bin/python3
"""this script print hello bnb
"""
from flask import Flask
import sys

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_word():
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    replace_space = text.replace("_", " ")
    show_text = (f"C {replace_space}")
    return show_text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_py_text(text='is cool'):
    replace_space = text.replace("_", " ")
    return (f"Python {replace_space}")


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    return (f"{n} is a number")


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=5000, debug=None)
