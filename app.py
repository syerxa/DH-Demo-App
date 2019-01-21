from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
import uuid

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
# Edit following line to configure the location of your mysql db
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
    modified = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'items': [i.to_dict() for i in self.items],
            'created': self.created,
            'modified': self.modified
        }
    
class Item(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    list_id = db.Column(db.String(36), db.ForeignKey('list.id'), nullable=False)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    
    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'list_id': self.list_id,
            'created': self.created,
            'modified': self.modified
        }
    
### EXCEPTIONS ###
def not_found(message):
    return (jsonify({'message': message, 'status_code': 404}), 404)

def bad_request(message):
    return (jsonify({'message': message, 'status_code': 400}), 400)

### API CALLS ###
# Get All Lists
@app.route('/lists', methods = ['GET'])
@cache.cached(timeout=30)
def get_lists():
    lists = List.query.order_by(List.created).all();
    return (jsonify({'lists': [list.to_dict() for list in lists]}), 200)

# Get Single List
@app.route('/lists/<list_id>', methods = ['GET'])
@cache.cached(timeout=30)
def get_list(list_id):
    l = List.query.filter_by(id=list_id).first()
    
    if l is None:
        return not_found('Could not locate list with id: {}'.format(list_id))
    
    return (jsonify(l.to_dict()), 200)
 
# Create List
@app.route('/lists', methods = ['POST'])
def create_list():
    data = request.get_json()
    
    l = List()
    l.id = str(uuid.uuid4())
    if 'title' in data:
        l.title = data['title']
    else:
        return bad_request('List missing required attribute: title')
    if 'description' in data:
        l.description = data['description']
    db.session.add(l)
    
    # Create Items for List
    if 'items' in data:
        items = data['items']
        for item in items:
            i = Item()
            i.id = str(uuid.uuid4())
            if 'description' in item:
                i.description = item['description']
            else:
                return bad_request('Item missing required attribute: description')
            if 'status' in item:
                if item['status'] == 'complete' or item['status'] == 'incomplete':
                    i.status = item['status']
                else:
                    return bad_request("Item attribute status does not contain a valid value. " +
                                       "Valid options are: 'complete' or 'incomplete'")
            else:
                i.status = 'incomplete'
            i.list_id = l.id
            db.session.add(i)
        
    db.session.commit()
    return (jsonify(l.to_dict()), 201)
 
# Update List
@app.route('/lists/<list_id>', methods = ['PUT'])
def update_list(list_id):
    data = request.get_json()
    l = List.query.filter_by(id=list_id).first()
    
    if l is None:
        return not_found('Could not locate list with id: {}'.format(list_id))
    
    if 'title' in data:
        l.title = data['title']
    else:
        return bad_request('List missing required attribute: title')
    if 'description' in data:
        l.description = data['description']
        
    db.session.commit()
    return (jsonify(l.to_dict()), 200)

# Delete List
@app.route('/lists/<list_id>', methods = ['DELETE'])
def delete_list(list_id):
    l = List.query.filter_by(id=list_id).first()
    
    if l is None:
        return not_found('Could not locate list with id: {}'.format(list_id))
    
    db.session.delete(l)
    db.session.commit()
    return ('', 204)

# Get All Items From List
@app.route('/lists/<l_id>/items', methods = ['GET'])
@cache.cached(timeout=30)
def get_items(l_id):
    items = Item.query.filter_by(list_id=l_id).order_by(Item.created).all()
    return (jsonify({'items': [item.to_dict() for item in items]}), 200)

# Get Single Item From List
@app.route('/lists/<l_id>/items/<item_id>', methods = ['GET'])
@cache.cached(timeout=30)
def get_item(l_id, item_id):
    i = Item.query.filter_by(id=item_id,list_id=l_id).first()
    
    if i is None:
        return not_found('Could not locate item with id: {}'.format(item_id))
    
    return (jsonify(i.to_dict()), 200)

# Create Item From List
@app.route('/lists/<l_id>/items', methods = ['POST'])
def create_item(l_id):
    data = request.get_json()
    
    i = Item()
    i.id = str(uuid.uuid4())
    if 'description' in data:
        i.description = data['description']
    else:
        return bad_request('Item missing required attribute: description')
    if 'status' in data:
        if data['status'] == 'complete' or data['status'] == 'incomplete':
            i.status = data['status']
        else:
            return bad_request("Item attribute status does not contain a valid value. " +
                               "Valid options are: 'complete' or 'incomplete'")
    else:
        i.status = 'incomplete'
        
    i.list_id = l_id
    db.session.add(i)
    db.session.commit()
    return (jsonify(i.to_dict()), 201)

# Update Item From List
@app.route('/lists/<l_id>/items/<item_id>', methods = ['PUT'])
def update_item(l_id, item_id):
    data = request.get_json()
    i = Item.query.filter_by(id=item_id,list_id=l_id).first()
    
    if i is None:
        return not_found('Could not locate item with id: {}'.format(item_id))
    
    if 'description' in data:
        i.description = data['description']
    else:
        return bad_request('Item missing required attribute: description')
    if 'status' in data:
        if data['status'] == 'complete' or data['status'] == 'incomplete':
            i.status = data['status']
        else:
            return bad_request("Item attribute status does not contain a valid value. " +
                               "Valid options are: 'complete' or 'incomplete'")
        
    db.session.commit()
    return (jsonify(i.to_dict()), 200)

# Delete Item From List
@app.route('/lists/<l_id>/items/<item_id>', methods = ['DELETE'])
def delete_item(l_id, item_id):
    i = Item.query.filter_by(id=item_id,list_id=l_id).first()
    
    if i is None:
        return not_found('Could not locate item with id: {}'.format(item_id))
    
    db.session.delete(i)
    db.session.commit()
    return ('', 204)