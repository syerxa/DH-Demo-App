from app import db

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