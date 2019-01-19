class List:
    
    def __init(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }