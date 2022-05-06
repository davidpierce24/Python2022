from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"


@app.route('/play')
def level1():
    return render_template("level3.html", x = 3)

@app.route('/play/<int:x>')
def level2(x):
    return render_template("level3.html", x = x)


@app.route('/play/<int:x>/<color>')
def level3(x, color):
    return render_template("level3.html", x = x, color = color)



if __name__ == "__main__":
    app.run(debug = True)