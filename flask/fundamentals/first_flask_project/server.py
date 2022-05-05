from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world :3'

@app.route('/another_route')
def another_route():
    return 'hey here"s my new route'

@app.route('/test/<route_data>')
def test_data(route_data):
    return f"the route data that was passed in was {route_data}"

@app.route('/multiply/<int:x>/<int:y>')
def multiply_two_numbers(x, y):
    return f"The result of {x} * {y} = {x*y}"

if __name__ == "__main__":
    app.run(debug = True)