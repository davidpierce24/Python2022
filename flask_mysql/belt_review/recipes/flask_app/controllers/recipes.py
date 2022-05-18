from flask_app import app

from flask import render_template, request, redirect, session, flash
from flask_app.models.recipe import Recipe


# Route to take user to edit recipe page
@app.route('/edit/recipe/<int:id>')
def to_recipe(id):
    if 'user_id' not in session:
        flash("You must log in to view this page")
        return redirect('/')

    return render_template("edit_recipe.html", id = id)



#  Route to edit recipe
@app.route('/edit/recipe', methods=["POST"])
def edit_recipe():

    data = {
        'id': request.form['id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'created_at': request.form['created_at'],
        'under_thirty': request.form['under_thirty']
    }

    Recipe.edit_recipe(data)

    return redirect('/dashboard')


# Route to delete recipe
@app.route('/delete/recipe/<int:id>')
def delete(id):

    data = {
        'id': id
    }

    Recipe.delete_recipe(data)

    return redirect('/dashboard')


# Route to take user to add new recipe page
@app.route('/to/add')
def to_add():
    if 'user_id' not in session:
        flash("You must log in to view this page")
        return redirect('/')

    return render_template('new_recipe.html')