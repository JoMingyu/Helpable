from flask import Flask
from flask_restful import Api

import account

app = Flask(__name__)
api = Api(app)

api.add_resource(account.SignUp, "/account/signup")
api.add_resource(account.SignIn, "/account/signin")

if __name__ == "__main__":
    print("-- Server Started")
    app.run()
