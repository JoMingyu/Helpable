from flask_restful import Resource
from flask import request, jsonify
from database import database
from database import query_formats


class SignUp(Resource):
    # 회원가입
    db = database.Database()

    def post(self):
        id = request.form['id']
        password = request.form['password']
        registration_key = request.form['token']
        name = request.form['name']
        age = request.form['age']
        type = request.form['type']
        gender = request.form['gender']
        phone_number = request.form['phone_number']
        password_question = request.form['password_question']
        password_answer = request.form['password_answer']
        # Not null 데이터들

        account = self.db.execute(query_formats.id_exist_check_format % id)
        if account:
            # id 존재
            return '', 409
        else:
            # id 미존재
            self.db.execute(query_formats.signup_primary_data_insert_format % (id, password, registration_key, name, int(age), int(type), gender, phone_number, password_question, password_answer))
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
    db = database.Database()

    def post(self):
        id = request.form['id']
        password = request.form['password']

        exist = self.db.execute(query_formats.id_exist_check_format % id)
        if exist:
            # id에 해당하는 계정 존재
            account = self.db.execute(query_formats.get_user_info_format % id)
            if account[0]['password'] == password:
                # 로그인 성공
                return '', 201
            else:
                return '', 404
        else:
            # 계정 미존재
            return '', 404


class Password(Resource):
    # 비밀번호 찾기
    db = database.Database()

    def get(self):
        # 질문 정보 제공
        id = request.args.get('id')

        user_info = self.db.execute(query_formats.get_user_info_format % id)
        data = {'question': user_info[0]['password_question'],
                'answer': user_info[0]['password_answer']}

        return jsonify(result=data)

    def post(self):
        # 비밀번호 변경
        id = request.form['id']
        password = request.form['password']

        self.db.execute(query_formats.password_change_format % (password, id))
        return '', 201


class Token(Resource):
    # 토큰 업데이트
    db = database.Database()

    def post(self):
        id = request.form['id']
        registration_key = request.form['token']

        self.db.execute(query_formats.registration_id_change_format % (registration_key, id))
        return '', 201
