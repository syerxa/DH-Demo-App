from app import db
from models.item import Item

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