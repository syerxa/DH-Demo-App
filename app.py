from flask import Flask, jsonify, request
from Models.list import List
import uuid

app = Flask(__name__)

db = {}

# Get All Lists
@app.route('/lists', methods = ['GET'])
def get_lists():
    return (jsonify(**db), 200)

# Get Single List
@app.route('/lists/<list_id>', methods = ['GET'])
def get_list(list_id):
    l = db[list_id]
    return (jsonify(l.serialize()), 200)

# Create List
@app.route('/lists', methods = ['POST'])
def create_list():
    data = request.get_json()
    l = List()
    l.id = str(uuid.uuid4())
    l.title = data['title']
    l.description = data['description']
    db[l.id] = l
    return (jsonify(l.serialize()), 201)

# Update List
@app.route('/lists/<list_id>', methods = ['PUT'])
def update_list(list_id):
    data = request.get_json()
    l = List()
    l.id = list_id
    l.title = data['title']
    l.description = data['description']
    db[l.id] = l
    return (jsonify(l.serialize()), 200)

# Delete List
@app.route('/lists/<list_id>', methods = ['DELETE'])
def delete_list(list_id):
    db.pop(list_id)
    return ('', 204)

# Get All Items From List
@app.route('/lists/<list_id>/items', methods = ['GET'])
def get_items(list_id):
    return 'This is the GET items endpoint for {}'.format(list_id)

# Get Single Item From List
@app.route('/lists/<list_id>/items/<item_id>', methods = ['GET'])
def get_item(list_id, item_id):
    return 'This is the GET item {} endpoint for {}'.format(item_id, list_id)

# Create Item From List
@app.route('/lists/<list_id>/items', methods = ['POST'])
def create_item(list_id):
    return 'This is the CREATE items endpoint for {}'.format(list_id)

# Update Item From List
@app.route('/lists/<list_id>/items/<item_id>', methods = ['PUT'])
def update_item(list_id, item_id):
    return 'This is the UPDATE item {} endpoint for {}'.format(item_id, list_id)

# Delete Item From List
@app.route('/lists/<list_id>/items/<item_id>', methods = ['DELETE'])
def delete_item(list_id, item_id):
    return 'This is the DELETE item {} endpoint for {}'.format(item_id, list_id)