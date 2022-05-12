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



















if __name__ == "__main__":
    app.run(debug=True)