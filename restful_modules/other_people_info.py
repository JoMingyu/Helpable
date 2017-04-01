from flask_restful import Resource
from flask import request
from database import Database
import query_formats


class PersonInfo(Resource):
    db = Database()

    def post(self):
        id = request.form['id']

        rows = self.db.execute(query_formats.get_other_person_info_format % id)
        for row in rows:
            pass