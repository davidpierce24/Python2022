# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL


# model the class after the user table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Using a class method to query our database
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM users;"

        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users



    # Method to create a user
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, updated_at, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('users_schema').query_db(query, data)



    # Method to show a single user
    @classmethod
    def show_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results =  connectToMySQL('users_schema').query_db(query, data)
        show = []
        for user in results:
            show.append(cls(user))
        return show



    # Method to edit a user
    @classmethod
    def edit_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL('users_schema').query_db(query, data)


    # @classmethod
    # def get_id(cls, data):
    #     query = "SELECT id FROM users WHERE first_name = %(first_name)s;"
    #     results =  connectToMySQL('users_schema').query_db(query, data)
    #     return results

    
    # Method to delete a user
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL('users_schema').query_db(query, data)
