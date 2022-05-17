from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask import render_template, redirect, request, session
from flask_app.models.user import User


# Route to render home page
@app.route('/')
def index():

    return render_template("index.html")


# Route to process user registration
@app.route('/users/register', methods=['POST'])
def register_user():

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

    return redirect('/success')