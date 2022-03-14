from flask import Flask, render_template

SECRET_MESSAGE = "FLUFFy tail"

app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return "You are in an login page"

@app.route("/<name>")
def hello_name(name):
    return "Hello, {escape(name)}"
