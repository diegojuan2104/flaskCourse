from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from security import authenticate, identity
from resources.user import UserRegister,User,UserLogin, TokenRefresh
from resources.item import Item, ItemList
from resources.store import Store,StoreList

app = Flask(__name__) #This means that this it's the main doc where flask runs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # To locate the db doc, and add sqlite,postgreSQL,Oracle whatever....
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app) #Allow add Resources from flask Rest-full
app.secret_key = '123456789123456789qwewqqwer'

@app.before_first_request #To Create all the tables before run 
def create_tables():
    db.create_all()

jwt = JWTManager(app) #JWTManager It's doesn't creating /auth endpoint
@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin':True}
    return {'is_admin':False}


@jwt.expired_token_loader
def expired_token_loader():
    return {
        "description":"The token has expired"
    }, 401 

@jwt.invalid_token_loader
def invalid_token_callback():
    return {
        "description":"The token is invalid "
    }, 401 

#Add all the resources 
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')
api.add_resource(StoreList,'/stores')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(User,'/user/<int:user_id>')
api.add_resource(UserLogin,'/login')
api.add_resource(TokenRefresh,'/refresh')
# Allows only run in app.py
if __name__ == '__main__':
    from db import db 
    db.init_app(app)
    app.run(port = 3000, debug=True)