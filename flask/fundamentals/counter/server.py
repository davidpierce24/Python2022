from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "howdoidothis"

@app.route('/')
def index():
    
    # if 'visits' in session:
    #     print('key exists!')
    #     print(session['visits'])
    if session.get('visits') is None:
        session['visits'] = 1

    else:
        session['visits'] +=1
        print(session)

    # else:
    #     print("key 'full_name' does NOT exist")
    

    #     var = session.get('visits')
    #     var += 1

    # session['visits'] = var



    return render_template('index.html')

# @app.route('/process')
# def process():

#     session['load'] = request.form['load']

#     if 'full_name' in session:
#         print('key exists!')
#     else:
#         print("key 'load' does NOT exist")

#     # return render_template('index.html')









if __name__ == "__main__":
    app.run(debug = True)
