from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL


class Archive:
    DB_NAME = "apod_schema"
    def __init__(self, date):
        self.date = date

    @classmethod
    def create(cls, data):
        query = "INSERT INTO user_archive (date, user_id, created_at, updated_at) VALUES (%(date)s, %(user_id)s, NOW(), NOW())"

        return connectToMySQL(cls.DB_NAME).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM user_archive WHERE user_id = %(user_id)s AND date = %(date)s"
        result = connectToMySQL(cls.DB_NAME).query_db(query, data)

        if (len(result) < 1):
            return False

        apod = cls(result[0])
        return apod

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM user_archive WHERE user_id = %(user_id)s ORDER BY date DESC"
        result = connectToMySQL(cls.DB_NAME).query_db(query, data)

        dates = []
        for apod in result:
            dates.append(apod['date'])

        return dates

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM user_archive WHERE user_id = %(user_id)s AND date = %(date)s"
        
        return connectToMySQL(cls.DB_NAME).query_db(query, data)

