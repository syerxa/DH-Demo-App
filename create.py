from app import db, List, Item

db.drop_all()
db.create_all()
list1 = List(id='demoid', title='Demo Title', description='This is a Description')
list2 = List(id='demoid2', title='Demo Title2', description='This is also a Description')
db.session.add(list1)
db.session.add(list2)
db.session.commit()
