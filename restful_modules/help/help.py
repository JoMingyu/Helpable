from flask_restful import Resource
from flask import request
from database import Database
import query_formats
from firebase import firebase_push


class HelpRequest(Resource):
    db = Database()
    sender = firebase_push.FCMSender('AAAA9LkX9Zs:APA91bHyu886FvO46OzqQLkBofJfxpszMI9_HpBrMTPkTed46hzsColH0K9sloVNRaiRwszAn17eDPfue5-KtzS0Q0gPekTgyzRa1CjgbpBathxpD6OH0lsj8CHDJVt8DDRQuVu8_Xjh')

    def post(self):
        # 도움 요청
        id = request.form['id']
        longitude = request.form['longi']
        latitude = request.form['lati']

        self.db.execute(query_formats.request_help_format % (id, longitude, latitude))
        user_info = self.db.execute(query_formats.get_user_data_format % id)
        for row in user_info:
            self.sender.send(row['name'] + '님이 도움을 요청합니다',
                             '',
                             '')
        return '', 201

    def get(self):
        # 기여자가 열람 가능한 도움 요청 정보
        id = request.args.get('id')

        # help = self.db.execute(query_formats.)
        pass

    def delete(self):
        # 도움 요청 취소
        pass


class HelpResponse(Resource):
    db = Database()

    def post(self):
        # 기여자 등록
        pass

    def get(self):
        # 도움 요청자가 열람 가능한 기여자 목록
        pass

    def delete(self):
        # 기여 취소
        pass


class Accept(Resource):
    db = Database()

    def post(self):
        # 도움 요청자의 기여자 선정
        pass


class Completion(Resource):
    db = Database()

    def post(self):
        # 도움 완료
        pass
