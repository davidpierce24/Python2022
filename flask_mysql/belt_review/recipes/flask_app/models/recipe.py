from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user


#class for recipes
class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.user = {}



     # Method to display recipes with user data
    @classmethod
    def get_recipes_with_user(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;"

        results = connectToMySQL('recipes_schema').query_db(query)

        all_recipes = []

        for row in results:
            recipes = cls(row)

            data = {
                'id': row['id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            recipes.user = user.User(data)
            all_recipes.append(recipes)

        return all_recipes


    # Method to edit a recipe
    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under_thirty = %(under_thirty)s, created_at = %(created_at)s WHERE id = %(id)s;"
        connectToMySQL('recipes_schema').query_db(query, data)


    # Method to delete a recipe
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        connectToMySQL('recipes_schema').query_db(query, data)



    # Method to create recipe
    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under_thirty, created_at, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_thirty)s, %(created_at)s, %(user_id)s);"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return results
