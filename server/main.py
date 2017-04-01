from flask import Flask
from flask_restful import Api

import index_for_test
from user import account
from user import user_info
from user import profile_picture

app = Flask(__name__)
api = Api(app)

api.add_resource(account.SignUp, "/account/signup")
api.add_resource(account.SignIn, "/account/signin")
api.add_resource(profile_picture.ProfilePicture, "/account/profile-picture")
api.add_resource(user_info.PersonInfo, "/account/person-info")
api.add_resource(index_for_test.Index, "/")

if __name__ == "__main__":
    print("-- Server Started")
    # app.run('youngjae1047.cafe24.com')
    app.run('30.0.1.245')
