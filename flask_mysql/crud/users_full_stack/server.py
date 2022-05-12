from flask import Flask, render_template, request, redirect


# import the class from user.py
from user import User


app = Flask(__name__)

# Route to render all users
@app.route('/')
def all_users():

    users = User.get_all()
    print(users)
    return render_template("read_all.html", users = users)

@app.route('/add_user')
def create_user():

    return render_template("create.html")


# Route to add a new user
@app.route('/process', methods = ["POST"])
def add_user():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }

    User.create_user(data)

    return redirect('/')










if __name__ == "__main__":
    app.run(debug=True)