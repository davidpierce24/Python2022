from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/results', methods = ['post'])
# def receive_form():
#     print(request.form)
#     return redirect('/')

@app.route('/result', methods = ['post'])
def receive_form():
    
    return render_template('result.html', full_name = request.form['full_name'], social_security = request.form['social_security'])

if __name__ == "__main__":
    app.run(debug = True)