from flask_restful import Resource
from flask import request
from database import Database
import query_formats
from firebase import firebase_push


class Help(Resource):
    db = Database()

    def post(self):
        id = request.form['id']
        longitude = request.form['longi']
        latitude = request.form['lati']

        self.db.execute(query_formats.request_help_format % (id, longitude, latitude))
        sender = firebase_push.FCMSender('AAAA9LkX9Zs:APA91bHyu886FvO46OzqQLkBofJfxpszMI9_HpBrMTPkTed46hzsColH0K9sloVNRaiRwszAn17eDPfue5-KtzS0Q0gPekTgyzRa1CjgbpBathxpD6OH0lsj8CHDJVt8DDRQuVu8_Xjh')
        return '', 201

    def get(self):
        id = request.args.get('id')

        # help = self.db.execute(query_formats.)