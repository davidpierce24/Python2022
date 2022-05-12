from flask_app import app

from flask import Flask, render_template, request, redirect


# import the class from friend.py
from flask_app.models.friend import Friend


# Route to render all friends
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

# Route to create a friend
@app.route('/create', methods=["POST"])
def create_friend():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }

    Friend.create_friend(data)

    return redirect("/")


# Route to render update form
@app.route('/renderUpdate/<int:id>')
def render_update(id):



    return render_template('update.html', id =  id)



# Route to update a friend
@app.route('/update', methods=["POST"])
def update():

    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }

    Friend.update_friend(data)
    
    return redirect('/')


# Route to delete a friend
@app.route("/delete/<int:id>")
def delete(id):

    data = {
        'id': id
    }

    Friend.delete_friend(data)
    return redirect('/')