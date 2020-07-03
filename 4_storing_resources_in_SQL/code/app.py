from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList


app = Flask(__name__)
api = Api(app)
app.secret_key = '123456789123456789qwewqqwer'

jwt = JWT(app, authenticate, identity)



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')


# allows only run in app.py
if __name__ == '__main__':
    app.run(port = 3000, debug=True)