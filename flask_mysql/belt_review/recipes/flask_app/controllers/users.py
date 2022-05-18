from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

# Route to render the login and registration page
@app.route('/')
def home():

    return render_template("login.html")


# Route to process user registration
@app.route('/register', methods=["POST"])
def register():

    # validate user
    if not User.validate_user(request.form):
        return redirect('/')


    # then if valid, add to DB
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    user_id = User.add_user(data)

    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']


    return redirect('/dashboard')



# Route to process user login
@app.route('/login', methods=["POST"])
def login():

    email_input = { "email" : request.form["email"] }
    users = User.get_by_email(email_input)
    
    if len(users) != 1:
        flash("Invalid Email/Password")
        return redirect('/')

    user = users[0]

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')

    session['user_id'] = user.id
    session['first_name'] = user.first_name

    return redirect('/dashboard')


# Route to successful registration or login
@app.route('/dashboard')
def success():
    if 'user_id' not in session:
        flash("You must log in to view this page")
        return redirect('/')

    print (session['user_id'])


    recipes = Recipe.get_recipes_with_user()

    return render_template("dashboard.html", recipes = recipes)



# Route to logout user
@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')