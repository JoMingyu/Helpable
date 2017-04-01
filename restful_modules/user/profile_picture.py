from flask_restful import Resource
from flask import request, send_from_directory
import os


class ProfilePicture(Resource):
    # 프로필 사진 업로드
    def post(self):
        id = request.form['id']
        file = request.files['profile_picture']
        extension = file.filename.split('.')[1]

        file.save('../profile_pictures/' + id + '.' + extension)
        return '', 201

    def get(self):
        id = request.args.get('id')

        file_names = os.listdir('../profile_pictures/')
        for file_name in file_names:
            if id in file_name:
                return send_from_directory('../profile_pictures/', file_name, as_attachment=True)
            else:
                continue

        return '', 404
