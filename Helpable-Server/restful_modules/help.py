from flask_restful import Resource
from flask import request, jsonify
from database import database, query_formats
from firebase import firebase_push


class HelpRequest(Resource):
    db = database.Database()
    sender = firebase_push.FCMSender('AIzaSyDEqNM3DgDvmxryb2pDrjry5wLHuT8NPjI')

    def post(self):
        # 도움 요청
        id = request.form['id']
        longitude = request.form['longi']
        latitude = request.form['lati']
        content = request.form['content']

        user_info = self.db.execute(query_formats.get_user_info_format % id)
        self.db.execute(query_formats.request_help_format % (id, user_info[0]['registration_key'], float(longitude), float(latitude), content))
        self.sender.send('Helpable',
                         user_info[0]['name'] + '님에게 도움이 필요합니다.')

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

        return jsonify(result=help_list)

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
    db = database.Database()

    def post(self):
        # 기여자 등록
        id = request.form['id']
        idx = request.form['idx']

        self.db.execute(query_formats.response_help_format % (int(idx), id))
        requester_info = self.db.execute(query_formats.get_help_format % idx)
        requester_key = requester_info[0]['requester_key']
        # self.sender.send('Helpable',
        #                  '도우미가 나타났습니다.',
        #                  requester_key)
        self.sender.send('Helpable',
                         '도우미가 나타났습니다.')
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
                'id': row['contributor_id'],
                'name': user_info[0]['name'],
                'age': user_info[0]['age'],
                'gender': user_info[0]['gender'],
                'affiliation': user_info[0]['affiliation']
            }
            contributor_list.append(data)

        return jsonify(result=contributor_list)

    def delete(self):
        # 기여 취소
        id = request.form['id']
        idx = request.form['idx']

        self.db.execute(query_formats.delete_contributor_format % (int(idx), id))

        return '', 200


class Accept(Resource):
    # 기여자 선정
    db = database.Database()

    def post(self):
        id = request.form['id']
        idx = request.form['idx']

        self.db.execute(query_formats.select_contributor_format % (id, int(idx)))
        user_info = self.db.execute(query_formats.get_user_info_format % id)
        contributor_key = user_info[0]['registration_key']
        # self.sender.send('Helpable - 도우미',
        #                  '당신의 도움으로 차별없는 세상을 만들어주세요.',
        #                  contributor_key)
        self.sender.send('Helpable - 도우미',
                         '당신의 도움으로 차별없는 세상을 만들어주세요.')

        return '', 201


class Connect(Resource):
    db = database.Database()

    def get(self):
        # 상대방 정보 조회
        pass


class Completion(Resource):
    db = database.Database()

    def post(self):
        # 도움 완료
        pass
