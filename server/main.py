from flask import Flask
from flask_restful import Api

import account

import index_for_test

app = Flask(__name__)
api = Api(app)

api.add_resource
api.add_resource(account.SignUp, "/account/signup")
api.add_resource(account.SignIn, "/account/signin")
api.add_resource(index_for_test.Index, "/")

if __name__ == "__main__":
    print("-- Server Started")
    # app.run('youngjae1047.cafe24.com')
    app.run('30.0.1.245')
