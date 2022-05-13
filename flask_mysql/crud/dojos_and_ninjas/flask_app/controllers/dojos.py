from flask_app import app

from flask import render_template, redirect, session, request

from flask_app.models.dojo import Dojo


@app.route('/')
def home():

    dojos = Dojo.get_all()
    print(dojos)

    return render_template("dojos.html", dojos = dojos)