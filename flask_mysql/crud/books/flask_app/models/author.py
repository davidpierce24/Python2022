from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import book


# Model class after authors table in database
class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    
    # Method to show all authors
    @classmethod
    def show_all_authors(cls):
        query = "SELECT * FROM authors;"

        results = connectToMySQL('books_schema').query_db(query)

        return results



    # Method to add an author
    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"

        results = connectToMySQL('books_schema').query_db(query, data)

        return results