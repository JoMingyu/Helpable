from flask_restful import Resource
from flask import request


class Index(Resource):
    def post(self):
        file = request.files['test']
        print(file.filename)
        file.save('../profile_pictures/' + file.filename)
        return '', 201
