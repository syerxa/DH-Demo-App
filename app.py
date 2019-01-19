from flask import Flask

app = Flask(__name__)

# Get All Lists
@app.route('/lists', methods = ['GET'])
def get_lists():
    return 'This is the GET ALL endpoint'

# Get Single List
@app.route('/lists/<list_id>', methods = ['GET'])
def get_list(list_id):
    return 'This is the GET endpoint for {}'.format(list_id)

# Create List
@app.route('/lists', methods = ['POST'])
def create_list():
    return 'This is the CREATE endpoint'

# Update List
@app.route('/lists/<list_id>', methods = ['PUT'])
def update_list(list_id):
    return 'This is the UPDATE endpoint for {}'.format(list_id)

# Delete List
@app.route('/lists/<list_id>', methods = ['DELETE'])
def delete_list(list_id):
    return 'This is the DELETE endpoint for {}'.format(list_id)

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

# Hello World
@app.route('/')
def hello():
    return 'Hello, World!'