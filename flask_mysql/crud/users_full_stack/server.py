from flask import Flask, render_template, request, redirect


# import the class from user.py
from user import User


app = Flask(__name__)





















if __name__ == "__main__":
    app.run(debug=True)