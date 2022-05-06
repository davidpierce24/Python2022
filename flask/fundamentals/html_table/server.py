from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def table():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    list = []
    list2 = []

    for user in users:
        list.append(user)
        list2.append(user['first_name'] + " " + user['last_name'])

    return render_template("index.html", list = list, list2 = list2)









if __name__ == "__main__":
    app.run(debug = True)