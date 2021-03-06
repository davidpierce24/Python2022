from flask import render_template, request, redirect, session

from flask_app import app

# import the class from user.py
from flask_app.models.user import User

# Route to render all users
@app.route('/')
def all_users():

    users = User.get_all()
    print(users)
    return render_template("read_all.html", users = users)



# Route that directs you to page for adding a user
@app.route('/add_user')
def create_user():

    return render_template("create.html")


# Route that directs you to page for showing user
@app.route('/show_user/<int:id>')
def show_user(id):
    
    data = {
        'id': id
    }

    show = User.show_user(data)

    return render_template("read_one.html", show = show, id = id)


# Route that directs you to a page to edit a user
@app.route('/edit_user/<int:id>')
def edit_user(id):

    data = {
        'id': id
    }

    show = User.show_user(data)
    print(show)

    return render_template("edit_user.html", id = id, show = show)


# Route to add a new user
@app.route('/process_add', methods = ["POST"])
def add_user():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    keep = User.create_user(data)


    return redirect(f'/show_user/{keep}')


# Route to edit a user
@app.route('/process_edit', methods = ["POST"])
def change_user():


    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    # id = request.form['id']
    # both of these ways can access id

    User.edit_user(data)

    return redirect(f'/show_user/{data["id"]}')


# Route to destroy a user
@app.route('/delete/<int:id>')
def destroy(id):

    data = {
        'id' : id
    }

    User.delete_user(data)
    return redirect('/')