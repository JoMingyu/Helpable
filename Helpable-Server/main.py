from flask import Flask
from flask_restful import Api

from restful_modules import account
from restful_modules import help
from restful_modules import profile_picture
from restful_modules import user_info

app = Flask(__name__)
api = Api(app)

api.add_resource(account.SignUp, "/account/signup")
api.add_resource(account.SignIn, "/account/signin")
api.add_resource(account.Password, "/account/password")
api.add_resource(account.Token, "/account/token")

api.add_resource(profile_picture.ProfilePicture, "/account/profile-picture")
api.add_resource(user_info.UserInfo, "/account/user-info")

api.add_resource(help.HelpRequest, "/help/request")
api.add_resource(help.HelpResponse, "/help/response")
api.add_resource(help.Accept, "/help/accept")
api.add_resource(help.Completion, "/help/completion")

if __name__ == "__main__":
    print("-- Server Started")
    app.run('0.0.0.0')
