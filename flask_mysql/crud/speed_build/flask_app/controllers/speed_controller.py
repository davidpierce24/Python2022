from winreg import REG_DWORD_BIG_ENDIAN
from flask_app import app

from flask import render_template

@app.route('/')
def index():

    return render_template("index.html")