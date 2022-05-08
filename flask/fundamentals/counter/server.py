from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "howdoidothis"

@app.route('/')
def index():
    if session.get('visits') is None:
        session['visits'] = 1
    else:
        session['visits'] +=1
        print(session)
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/count', methods = ['post'])
def count():
    session['visits'] +=1
    return redirect('/')

@app.route('/reset', methods = ['post'])
def reset():
    return redirect('/destroy_session')




if __name__ == "__main__":
    app.run(debug = True)
