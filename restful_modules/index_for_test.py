from flask_restful import Resource
from flask import request


class Index(Resource):
    def post(self):
        test = request.form['test']
        return test, 201
