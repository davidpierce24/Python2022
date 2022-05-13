from flask_app import app

from flask import render_template, redirect, session, request

from flask_app.models.dojo import Dojo


# Home page route
@app.route('/')
def home():

    dojos = Dojo.get_all()
    print(dojos)

    return render_template("dojos.html", dojos = dojos)


# Route for adding a new dojo
@app.route('/process/dojo', methods = ['POST'])
def add_dojo():

    data = {
        'name': request.form['name']
    }

    Dojo.add_dojo(data)

    return redirect('/')



# Route for taking user to Add ninja page
@app.route('/add/ninja')
def add_ninja():

    dojos = Dojo.get_all()

    return render_template("ninja.html", dojos = dojos)

