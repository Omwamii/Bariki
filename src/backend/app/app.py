""" App main module """
from flask import Flask, redirect, request
from flask import render_template
from flask_login import LoginManager
from models.cause import Cause
from models.donor import Donor
from models.recipient import Recipient
from models.contract import Contract
import models.storage as db


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bariki.db"

# db.init_app(app)

@app.route("/")
def index():
    """ Index page """
    return render_template('index.html')

@app.route('/create_user/')
def create_user():
    """ Create user route """
    return "<h1>Create User</h1>"

@app.route("/signup")
def signup():
    """ Sign up page """
    return "<h1>Sign Up</h1>"

@app.route("/login")
def login():
    """ Login page """
    return "<h1>Login</h1>"

@app.route("/dashboard")
#@login_required
def dashboard():
    """ Dashboard page """
    return "<h1>Dashboard</h1>"

@app.route("/donate")
def donate():
    """ Donate page """
    return "<h1>Donate</h1>"

@app.route("/logout")
def logout():
    """ Logout """
    return "<h1> Home Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)