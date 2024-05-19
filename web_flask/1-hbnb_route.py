#!/usr/bin/python3
"""this script print hello bnb
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_word():
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    return ("HBNB")


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=5000, debug=None)
