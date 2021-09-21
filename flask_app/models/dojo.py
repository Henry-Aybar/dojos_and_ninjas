from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        return results

    @classmethod
    def new_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s,NOW(), NOW())"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results

    @classmethod
    def dojo_list(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        dojo = cls( results[0] )
        print(results)
        for row in results:
            ninja_data = {
                "id" : row['id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "age" : row['age'],
                "dojo_id" : row['dojo_id'],
                "created_at" : row['ninjas.created_at'],
                "updated_at" : row['ninjas.updated_at'],
            }
            dojo.ninjas.append( Ninja ( ninja_data ))
        return dojo