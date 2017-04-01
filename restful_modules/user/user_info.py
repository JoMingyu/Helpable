from flask_restful import Resource
from flask import request, json
from database import Database
import query_formats


class UserInfo(Resource):
    db = Database()

    def get(self):
        id = request.args.get('id')

        user_info = self.db.execute(query_formats.get_user_data_format % id)
        for row in user_info:
            if row['type'] == 1 or row['type'] == 2:
                data = {
                    'name': row['name'],
                    'age': row['age'],
                    'type': row['type'],
                    'gender': row['gender'],
                    'affiliation': row['affiliation']
                }

            elif row['type'] == 3:
                data = {
                    'name': row['name'],
                    'age': row['age'],
                    'type': row['type'],
                    'gender': row['gender'],
                    'disability_rating': row['disability_rating'],
                    'disability_type': row['disability_type']
                }
                pass

        user_contribution = self.db.execute(query_formats.get_user_contribution_format % id)
        for row in user_contribution:
            data['give'] = row['give']
            data['take'] = row['take']

        return json.dumps(data), 200
