from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:2Federate@localhost/dhdemo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

### MODELS ###
class List(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    items = db.relationship('Item', backref='list', lazy=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            #Items
            'created': self.created,
            'modified': self.modified
        }
    
class Item(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    list_id = db.Column(db.String(36), db.ForeignKey('list.id'), nullable=False)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'list_id': self.list_id,
            'created': self.created,
            'modified': self.modified
        }

### API CALLS ###
# Get All Lists
@app.route('/lists', methods = ['GET'])
def get_lists():
    lists = List.query.order_by(List.created).all();
    return (jsonify({'lists': [list.to_dict() for list in lists]}), 200)

# Get Single List
@app.route('/lists/<list_id>', methods = ['GET'])
def get_list(list_id):
    l = List.query.filter_by(id=list_id).first_or_404()
    return (jsonify(l.to_dict()), 200)
 
# Create List
@app.route('/lists', methods = ['POST'])
def create_list():
    data = request.get_json()
    l = List()
    l.id = str(uuid.uuid4())
    l.title = data['title']
    l.description = data['description']
    db.session.add(l)
    db.session.commit()
    return (jsonify(l.to_dict()), 201)
 
# Update List
@app.route('/lists/<list_id>', methods = ['PUT'])
def update_list(list_id):
    data = request.get_json()
    l = List.query.filter_by(id=list_id).first_or_404()
    l.title = data['title']
    l.description = data['description']
    db.session.commit()
    return (jsonify(l.to_dict()), 200)

# Delete List
@app.route('/lists/<list_id>', methods = ['DELETE'])
def delete_list(list_id):
    l = List.query.filter_by(id=list_id).first_or_404()
    db.session.delete(l)
    db.session.commit()
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