from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "i am that first secret key for that first demo in class"

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/results', methods = ['post'])
# def receive_form():
#     print(request.form)
#     return redirect('/')

@app.route('/result', methods = ['post'])
def receive_form():
    
    session['full_name'] = request.form['full_name']

    # return render_template('result.html', full_name = request.form['full_name'], social_security = request.form['social_security'])

    return redirect('/show_results')

@app.route('/show_results')
def show_results():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug = True)