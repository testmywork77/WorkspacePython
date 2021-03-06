# flask is module/package, Flask is Class, jsonify is method
# camelCase -module(i.e. file name), package, method
# Pascal - Class
from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Store1',
        'items': [
            {
                'name': 'Item1',
                'price': 15.99
            }
        ]
    }
]


# POST -used to receive data (from Server point of view)
# GET -used to send data back only (from Server point of view)
# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


# if __name__ == '__main__':
app.run(port=5000)
