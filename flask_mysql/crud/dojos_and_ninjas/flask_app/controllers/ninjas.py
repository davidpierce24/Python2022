from flask_app import app

from flask import render_template, redirect, session, request

from flask_app.models.ninja import Ninja


# Route to process new ninja
@app.route('/process/ninja', methods=["POST"])
def process_ninja():

    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }

    Ninja.add_ninja(data)

    return redirect(f'/show/dojo/{data["dojo_id"]}')


