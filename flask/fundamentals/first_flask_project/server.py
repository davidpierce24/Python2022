from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/another_route')
def another_route():
    return 'hey here"s my new route'

@app.route('/test/<route_data>')
def test_data(route_data):
    return f"the route data that was passed in was {route_data}"

@app.route('/multiply/<int:x>/<int:y>')
def multiply_two_numbers(x, y):
    return render_template("multiply.html", x_temp = x, y_temp = y, result = x*y)

@app.route('/multiplication_table/<int:x>/<int:y>')
def multiplication_table(x,y):
    results = []

    new_row = ["X"]
    for k in range(0, x+1):
        new_row.append(k)
    results.append(new_row)

    for i in range(0, y+1):
        new_row = [i]
        for j in range(0, x+1):
            new_row.append(i*j)
        results.append(new_row)
    print(results)
    return render_template("multitable.html", x = x, y = y, results = results)



if __name__ == "__main__":
    app.run(debug = True)