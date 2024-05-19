#!/usr/bin/python3
"""this script print hello bnb
"""
from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html_number(n):
    return render_template("5-number.html", number_pass=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_odd_or_even(n):
    if ((n % 2) == 0):
        return render_template("6-number_odd_or_even.html",
                               text_pass=(f"{n} is even"))
    else:
        return render_template("6-number_odd_or_even.html",
                               text_pass=(f"{n} is odd"))


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=5000, debug=None)
