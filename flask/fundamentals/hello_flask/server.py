from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<word>')
def say_word(word):
    return f"Hi {word}!"

@app.route('/repeat/<int:x>/<word>')
def repeat(word, x):
    # return word * x
    list = ""
    for item in range(0, x+1):
        list += f"{word}\r\n"
    return list

@app.route('/<word>')
def notwork(word):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

