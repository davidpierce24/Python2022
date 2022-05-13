from flask_app import app

from flask import render_template, redirect, session, request

# from flask_app.models.dojo import Dojo


@app.route('/')
def index():

    return render_template("dojos.html")