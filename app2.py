
from flask import Flask,jsonify
app = Flask(__name__)

stores=[
    {   'name':'MyStore',
        'items':[
                {'name':'MyItem',
                'price': 15.99
                }
                ]
    }
]

##### for a server ####
# POST - used to receive data
# GET - used to send data back only

@app.route('/')
def home():
    return "Hello Stores"

# POST /store data: {name}
@app.route('/store',methods=['POST'])
def create_store():
    pass    

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store():
    pass

# GET /store
@app.route('/store', methods=['GET'])
def get_all_stores():
    return jsonify({'stores': stores}) 


# POST /store/<string:name>/item{name:, price:}
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store():
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item',methods=['GET'])
def get_item_in_store():
    pass



app.run(port=5000)