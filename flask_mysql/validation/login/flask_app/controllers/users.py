from flask_app import app
from flask_bcrypt import Bcrypt

from flask import render_template, redirect, request, session


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/users/register', methods=['POST'])
def register_user():

    # validate user


    # then if valid, add to DB

    return('/')