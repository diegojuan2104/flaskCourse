import sqlite3
from flask_restful import Resource,reqparse

class User:


    def __init__(self, _id, username,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
           
            query ="SELECT * FROM users WHERE username = ?"
            #execute receives a tuple, that's whhy the ','
            result = cursor.execute(query,(username,))
            #get the first row
            row = result.fetchone()

            if row:
                user = cls(*row)
            else:
                 user = None

            connection.close()

            return user

    @classmethod
    def find_by_id(cls, _id):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
           

            query ="SELECT * FROM users WHERE id = ?"
            #execute receives a tuple, that's whhy the ','
            result = cursor.execute(query,(_id,))
            #get the first row
            row = result.fetchone()

            if row:
                user = cls(*row)
            else:
                 user = None

            connection.close()

            return user

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type= str, required=True, help="This field cannot be left blank!")
    parser.add_argument('password', type= str, required=True, help="This field cannot be left blank!")

    def post(self):
        data = UserRegister.parser.parse_args()

        if(User.find_by_username(data['username']) == None):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            query = "INSERT INTO users VALUES (NULL,?,?)"
            cursor.execute(query,(data['username'],data['password']))
            connection.commit()
            connection.close()
        else: 
            return{"message":"Username already exists!"},400

        return {"message":"User created sucessfully!"}, 201