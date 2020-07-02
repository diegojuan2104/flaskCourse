from flask import Flask, jsonify, request

stores = [
    {
        'name':'myStore',
        'items':[
            {
                'name':'item1',
                'price':23.99
            }
        ]
    }
]


app = Flask(__name__)

#POST /store data: 
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()

    new_store = {
        'name': request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)


#GET /store/name
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
    return jsonify({'message':'store not found'})

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


#POST store/name/item{name:, price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'items':request_data['price']
            }
        store['items'].append(new_item)
    
    return(jsonify(new_item))
    

#GET /store/name/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return "store not found!"
app.run(port = 5000)

