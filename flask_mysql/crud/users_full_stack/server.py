from flask import Flask, render_template, request, redirect, session


# import the class from user.py
from user import User


app = Flask(__name__)
app.secret_key = 'what the heck is going on'

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


    return render_template("edit_user.html", id = id)


# Route to add a new user
@app.route('/process_add', methods = ["POST"])
def add_user():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.create_user(data)
    id = User.get_id(data)
    
    print(id)

    id = 'id'

    return redirect('/show_user/<int:id>')


# Route to edit a user
@app.route('/process_edit', methods = ["POST"])
def change_user():

    # session['id'] = request.form['id']

    data = {
        'id': request.form['id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.edit_user(data)

    return redirect('/show_user/<int:id>')








if __name__ == "__main__":
    app.run(debug=True)