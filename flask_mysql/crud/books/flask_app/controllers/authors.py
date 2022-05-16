from flask_app import app

from flask import render_template, redirect, session, request

from flask_app.models.author import Author



# Route to render the main authors page
@app.route('/')
def show_authors():

    authors = Author.show_all_authors()

    return render_template("authors.html", authors = authors)



# Route to process new author
@app.route('/process/author', methods=["POST"])
def process_author():

    data = {
        'name': request.form['name']
    }

    Author.add_author(data)

    return redirect('/')