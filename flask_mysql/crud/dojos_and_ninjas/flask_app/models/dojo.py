from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja


# Dojo class modeled after the dojos table in our database 
class Dojo:
    def __init__ (self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []


    # Class method to query all dojos from database
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos



    # Class method for adding a new dojo
    @classmethod
    def add_dojo(cls, data):

        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)



    # Class method for combining dojo data with ninja data
    @classmethod
    def show_dojo(cls, data):

        query = "SELECT *  FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        dojo_list = cls( results[0] )

        for row in results:

            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojo_id': row['dojo_id']
            }
            dojo_list.ninjas.append(ninja.Ninja(ninja_data))

        print(dojo_list)
        
        return dojo_list