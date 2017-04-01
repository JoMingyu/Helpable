from flask_restful import Resource
from flask import request
from database import Database
import query_formats


class Help(Resource):
    db = Database()

    def post(self):
        id = request.form['id']
        longitude = request.form['longi']
        latitude = request.form['lati']

        self.db.execute(query_formats.request_help_format % (id, longitude, latitude))
        return '', 201