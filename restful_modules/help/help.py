from flask_restful import Resource
from flask import request, json
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
        content = request.form['content']

        self.db.execute(query_formats.request_help_format % (id, float(longitude), float(latitude), content))
        user_info = self.db.execute(query_formats.get_user_info_format % id)
        # for row in user_info:
        #     self.sender.send(row['name'] + '님이 도움을 요청합니다.',
        #                      content,
        #                      '')
        return '', 201

    def get(self):
        # 도움 요청 목록
        help_rows = self.db.execute(query_formats.get_help_list_format)
        help_list = []
        for row in help_rows:
            user_info = self.db.execute(query_formats.get_user_info_format % row['requester_id'])
            data = {
                'idx': row['idx'],
                'longi': row['longitude'],
                'lati': row['latitude'],
                'content': row['content'],
                'name': user_info[0]['name'],
                'age': user_info[0]['age'],
                'gender': user_info[0]['gender'],
                'disability_rating': user_info[0]['disability_rating'],
                'disability_type': user_info[0]['disability_type']
            }

            if row['contributor_id']:
                data['has_contributor'] = True

            help_list.append(data)

        return json.dumps(help_list)

    def delete(self):
        # 도움 요청 취소
        id = request.form['id']
        idx = request.form['idx']

        # 도움 요청의 주인이 맞는지 확인
        help = self.db.execute(query_formats.get_help_format % int(idx))
        if id == help[0]['requester_id']:
            self.db.execute(query_formats.delete_help_format % int(idx))
            return '', 200

        else:
            return '', 404


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
