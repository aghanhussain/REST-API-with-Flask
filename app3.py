
from flask import Flask,jsonify,request,render_template
app = Flask(__name__)

stores=[
    {   'name':'mystore',
        'items':[
                {'name':'myitem1',
                'price': 1.99
                },
                {'name':'myitem2',
                'price': 1.99
                },
                {'name':'myitem3',
                'price': 1.99
                }
                ]
    }
    ,
    {   'name':'yourstore',
        'items':[
                {'name':'youritem1',
                'price': 15.99
                },
                {'name':'youritem2',
                'price': 5.99
                },
                {'name':'youritem3',
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
    return render_template('index.html')

# POST /store data: {name}
@app.route('/stores',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'item':[]
    }  
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message':"Store not found"})
    

# GET /store
@app.route('/stores', methods=['GET'])
def get_all_stores():
    return jsonify({'stores': stores}) 


# POST /store/<string:name>/item{name:, price:}
@app.route('/store/<string:name>/items',methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':"Store not found"})
        

# GET /store/<string:name>/item
@app.route('/store/<string:name>/items',methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store['name']== name:
            return jsonify({'items':store['items']})

    return jsonify({'message':"No items found in store"})



app.run(port=5050)