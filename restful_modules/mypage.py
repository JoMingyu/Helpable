from flask_restful import Resource
from flask import request
from database import Database
import query_formats


class MyPage(Resource):
    def post(self):
        # REST 개념 상 GET 메소드로 해야 하지만 클라이언트에 맞춰서 POST로
        pass
