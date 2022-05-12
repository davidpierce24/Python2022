from flask_app.config.mysqlconnection import connectToMySQL




class Dog:
    def __init__ (self, data):
        self.id = data['id']
        self.type = data['type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def get_all_dogs(cls):
        query = "SELECT * FROM dogs"

        results = connectToMySQL('friends_schema').query_db(query)

        list_dogs = []

        for item in results:
            list_dogs.append( cls(item))

        return list_dogs