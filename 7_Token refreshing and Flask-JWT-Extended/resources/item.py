from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required,get_jwt_claims, jwt_optional, get_jwt_identity, fresh_jwt_required
from models.item import ItemModel

class Item(Resource):
    #Specify all the arguments  
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('store_id', type=int, required=True, help="This field cannot be left blank!")

    @jwt_required #jwt decorator, NO
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'},404
    
    @fresh_jwt_required
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message":f"item: {name} already exist"}
       
        #catch the arguments 
        data = Item.parser.parse_args()
       
        # **data -> arguments in order
        try:
            item = ItemModel(name, **data)
            item.save_to_db()
        except:
            return {"message":"An error ocurred"},500

        return item.json(), 201 
    
    @jwt_required
    def delete(self,name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return{"message":"Admin privilege required"}, 401
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return ({"Message":"Item deleted!"})


    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        
        if item is None:
            item = ItemModel(name,**data)
            return{"mesagge":"An error ocurred"},500
        else:
            item.price = ['price']
        item.save_to_db()
        return item.json()
    
class ItemList(Resource):
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        items = [item.json() for item in ItemModel.query.all()]
        if user_id:
            return {"items":items},200
        return {'items': [item['name'] for item in items],"message":"more data avalible if you login"}