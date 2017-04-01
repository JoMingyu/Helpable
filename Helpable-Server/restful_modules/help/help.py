from flask_restful import Resource
from flask import request, json
from database import Database
import query_formats
from firebase_push import FCMSender


class HelpRequest(Resource):
    db = Database()
    sender = FCMSender('AAAA9LkX9Zs:APA91bHyu886FvO46OzqQLkBofJfxpszMI9_HpBrMTPkTed46hzsColH0K9sloVNRaiRwszAn17eDPfue5-KtzS0Q0gPekTgyzRa1CjgbpBathxpD6OH0lsj8CHDJVt8DDRQuVu8_Xjh')

    def post(self):
        # 도움 요청
        id = request.form['id']
        longitude = request.form['longi']
        latitude = request.form['lati']
        content = request.form['content']

        user_info = self.db.execute(query_formats.get_user_info_format % id)
        self.db.execute(query_formats.request_help_format % (id, user_info[0]['registration_key'], float(longitude), float(latitude), content))
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

        return json.dumps(help_list), 200

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
        id = request.form['id']
        idx = request.form['idx']

        self.db.execute(query_formats.response_help_format % (int(idx), id))
        # 푸쉬
        return '', 201

    def get(self):
        # 도움 요청자가 열람 가능한 기여자 목록
        idx = request.args.get('idx')

        contributor_rows = self.db.execute(query_formats.get_contributor_list_format % int(idx))
        contributor_list = []
        for row in contributor_rows:
            user_info = self.db.execute(query_formats.get_user_info_format % row['contributor_id'])
            data = {
                'idx': row['idx'],
                'name': user_info[0]['name'],
                'age': user_info[0]['age'],
                'gender': user_info[0]['gender'],
                'affiliation': user_info[0]['affiliation']
            }
            contributor_list.append(data)

        return json.dumps(data), 200

    def delete(self):
        # 기여 취소
        idx = request.form['idx']
        id = request.form['id']

        self.db.execute(query_formats.delete_contributor_format % (int(idx), id))

        return '', 200


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
