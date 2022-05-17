from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Validation #################################################
    @staticmethod
    def validate_user(data):

        is_valid = True

        # checks to see if first name is only letters with at least 2 characters
        if len(data['first_name']) < 2:
            flash("Please ensure first name is longer than 1 letter")
            is_valid = False


        # checks to see if first name is only letters with at least 2 characters
        if len(data['last_name']) < 2:
            flash("Please ensure last name is longer than 1 letter")
            is_valid = False


        # checks to see if email is valid based on regular expression
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False


        # checks to see if email already exists in database
        email_input = { "email" : data["email"] }
        user_in_db = User.get_by_email(email_input)
        
        if len(user_in_db) != 0:
            flash("Email already exists")
            is_valid = False


        # checks to see if email was submitted
        if len(data['email']) < 1:
            flash("Please add a valid email")
            is_valid = False


        # checks to see if password is submitted
        if len(data['password']) < 1:
            flash("Please add a valid password")
            is_valid = False

        
        # checks to see if password confirmation mathces
        if data['password'] != data['confirm_password']:
            flash("Passwords must match exactly")
            is_valid = False

        return is_valid
    
    # ###############################################################


    # Method to add user to database
    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s;"
        results  = connectToMySQL('recipes_schema').query_db(query, data)
        return results