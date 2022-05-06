from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def check():
    return render_template("index.html", x = 8, y = 8)

@app.route('/<int:x>')
def check2(x):
    return render_template("index.html", x = x, y = x)

@app.route('/<int:x>/<int:y>')
def check3(x, y):
    return render_template("index.html", x = x, y = y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def check4(x, y, color1, color2):
    return render_template("index.html", x = x, y = y, color1 = color1, color2 = color2)

if __name__ == '__main__':
    app.run(debug = True)