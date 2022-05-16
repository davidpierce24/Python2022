from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import author


# model class after books table in database
class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.pages = data['pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    # model for showing all of the books
    @classmethod
    def show_all_books(cls):
        query = "SELECT * FROM books;"

        results = connectToMySQL('books_schema').query_db(query)

        return results