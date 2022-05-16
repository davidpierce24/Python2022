from curses import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flash


class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_user(data):

        is_valid = True

        # username must be a valid length
        if len(data['username']) < 3 or len(data['username']) > 20:
            is_valid = False
            flash()