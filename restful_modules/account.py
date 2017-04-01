from flask_restful import Resource
from flask import request
from database import Database
import query_formats


class SignUp(Resource):
    # 회원가입
    db = Database()

    def post(self):
        id = request.form['id']
        password = request.form['password']
        registration_key = request.form['token']
        name = request.form['name']
        age = request.form['age']
        type = request.form['type']
        gender = request.form['gender']
        # Not null 데이터들

        print('Requested', id, password)

        rows = self.db.execute(query_formats.id_exist_check_format % id)
        if rows:
            # id 존재
            return '', 409
        else:
            # id 미존재
            self.db.execute(query_formats.signup_primary_data_insert_format % (id, password, registration_key, name, int(age), int(type), gender))
            self.db.execute(query_formats.person_contribution_initialize_format % id)
            if type == '1' or type == '2':
                # 일반인
                affiliation = request.form['affiliation']
                self.db.execute(query_formats.ordinary_person_signup_format % (affiliation, id))
                return '', 201

            elif type == '3':
                # 장애인
                disability_rating = request.form['disability_rating']
                disability_type = request.form['disability_type']
                self.db.execute(query_formats.disabled_person_signup_format % (int(disability_rating), disability_type, id))
                return '', 201


class SignIn(Resource):
    # 로그인
    db = Database()

    def post(self):
        id = request.form['id']
        password = request.form['password']

        rows = self.db.execute("SELECT * FROM account WHERE id='", id, "'")
        if rows:
            # id에 해당하는 계정 존재
            if rows[0]['password'] == password:
                # 로그인 성공
                return 'success', 201
            else:
                return '', 404
        else:
            # 계정 미존재
            return '', 404
