from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome_page():
    """returns a demo message"""
    return "welcome"


@app.route("/welcome/home")
def welcome_home():
    """ returns a demo message"""
    return "welcome home"

@app.route("/welcome/back")
def welcome_back():
    """returns a demo message"""
    return "welcome back"
