# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the users table from our database
class User:
    DB_NAME = "DB_NAME"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB_NAME).query_db(query)

        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM users WHERE users.id = %(id)s"

        return connectToMySQL(cls.DB_NAME).query_db(query, id)

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW())"

        return connectToMySQL(cls.DB_NAME).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE users.id = %(id)s"

        return connectToMySQL(cls.DB_NAME).query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM users WHERE users.id = %(id)s"

        return connectToMySQL(cls.DB_NAME).query_db(query, id)