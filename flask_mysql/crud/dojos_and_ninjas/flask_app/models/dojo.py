from flask_app.config.mysqlconnection import connectToMySQL


# Dojo class modeled after the dojos table in our database 
class Dojo:
    def __init__ (self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']




    # Class method to query all dojos from database
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos