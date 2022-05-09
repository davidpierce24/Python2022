from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "another one of these things for the dojo survey assignment"

@app.route('/')
def index():


    return render_template("index.html")

@app.route('/process', methods = ['post'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result') 

@app.route('/result')
def result():

    return render_template("result.html")

@app.route('/reset', methods = ['post'])
def reset():

    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True)