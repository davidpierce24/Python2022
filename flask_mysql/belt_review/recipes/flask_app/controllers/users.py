from crypt import methods
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask import render_template, redirect, request, session, flash
# from flask_app.models.user import User

# Route to render the login and registration page
@app.route('/')
def home():

    return render_template("login.html")


# Route to process user registration
@app.route('/register', methods=["POST"])
def register():



    return redirect('/')





# Route to process user login
@app.route('/login', methods=["POST"])
def login():



    return redirect('/')