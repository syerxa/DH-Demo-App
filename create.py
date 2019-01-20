from app import db, List, Item

db.drop_all()
db.create_all()

list1 = List(id='ce3583a6-17ea-472f-9cec-cc575eb3c687', title='Demo Title', description='This is a Description')
list2 = List(id='e3e9f7d7-1d21-4236-9251-c58c0f3c1f8c', title='Grocery List', description='Buy these things at the store')

item1 = Item(id='074351c8-acb7-475c-935c-ffae8524cb5a', description='Eggs', status='incomplete', list_id='e3e9f7d7-1d21-4236-9251-c58c0f3c1f8c')
item2 = Item(id='e8b7a7c7-e440-4722-bb03-b9960824ae88', description='Bacon', status='complete', list_id='e3e9f7d7-1d21-4236-9251-c58c0f3c1f8c')
item3 = Item(id='12a639a2-eb80-4aea-b173-fb804cacc8dd', description='Milk', status='incomplete', list_id='e3e9f7d7-1d21-4236-9251-c58c0f3c1f8c')
item4 = Item(id='1fac89af-d073-4384-bb9e-e725c618bff6', description='Cheese', status='incomplete', list_id='e3e9f7d7-1d21-4236-9251-c58c0f3c1f8c')

item5 = Item(id='1b575cdb-a06c-44cf-8931-6dee69926ab5', description='Item One', status='incomplete', list_id='ce3583a6-17ea-472f-9cec-cc575eb3c687')
item6 = Item(id='8ee132fb-f07d-4489-b4b2-8d244aee4986', description='Item Two', status='complete', list_id='ce3583a6-17ea-472f-9cec-cc575eb3c687')

db.session.add(list1)
db.session.add(list2)
db.session.add(item1)
db.session.add(item2)
db.session.add(item3)
db.session.add(item4)
db.session.add(item5)
db.session.add(item6)

db.session.commit()
