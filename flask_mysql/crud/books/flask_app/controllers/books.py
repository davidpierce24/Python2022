from flask_app import app

from flask import render_template, redirect, request, session

from flask_app.models.book import Book



# Route to render books main page
@app.route('/books')
def show_books():

    books = Book.show_all_books()

    return render_template("books.html", books = books)



# Route to process a new book
@app.route('/process/book', methods=["POST"])
def add_book():

    data = {
        'title': request.form['title'],
        'pages': request.form['pages']
    }

    Book.add_book(data)

    return redirect('/books')