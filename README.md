# DH Demo App - ToDo List API

This project is a technical Demo App of a simple ToDo List JSON API using Flask and SQLAlchemy.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The following are needed in order to successfully run the app on your local machine

```
Give examples
```

### Installing

Edit line 13 of app/__init__.py to point to your local MySQL database

```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@localhost/<database>'
```

Run the migration.py script to create the tables and seed data in your database.  Run the following command from the root of the project.

```
python3 migration.py
```

Finally, start the flask server from the root directory.

```
FLASK_APP=main.py flask run
```

## Running the tests

The unit tests can be run from the root directory with the following command

```
pytest
```

## API Calls

You can use the included postman collection or the following cURL commands to access the API endpoints.

**Get Lists**
```
curl -X GET \
  http://localhost:5000/lists \
  -H 'Postman-Token: 7e14173a-0f4f-4223-9720-d4a8c8c44bb6' \
  -H 'cache-control: no-cache'
```

**Get List**
```
curl -X GET \
  http://localhost:5000/lists/%3Clist_id%3E \
  -H 'Postman-Token: 9f15e6b8-4298-44e0-8c36-441dca985e93' \
  -H 'cache-control: no-cache'
```

**Create List**
```
curl -X POST \
  http://localhost:5000/lists \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 5af7226a-bdb8-4861-a598-01e60a73631c' \
  -H 'cache-control: no-cache' \
  -d '{
	"description": "My Todo List",
	"title": "TODO",
	"items": [{
		"description": "TODO 1",
		"status": "incomplete"
	}, {
		"description": "TODO 2",
		"status": "incomplete"
	}]
}'
```

**Update List**
```
curl -X PUT \
  http://localhost:5000/lists/%3Clist_id%3E \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: f85a31dc-1b28-4dc1-aa75-a87f422b223b' \
  -H 'cache-control: no-cache' \
  -d '{
	"description": "My Todo List Updated",
	"title": "TODO Updated"
}'
```

**Delete List**
```
curl -X DELETE \
  http://localhost:5000/lists/%3Clist_d%3E \
  -H 'Postman-Token: 4e4d67b3-b139-4ca5-854e-1fba37d5aad3' \
  -H 'cache-control: no-cache'
```

**Get Items from List**
```
curl -X GET \
  http://localhost:5000/lists/%3Clist_id%3E/items \
  -H 'Postman-Token: 2561a46a-d33c-4250-8b07-7dcbbc9e428c' \
  -H 'cache-control: no-cache'
```

**Get Item**
```
curl -X GET \
  http://localhost:5000/lists/%3Clist_id%3E/items/%3Citem_id%3E \
  -H 'Postman-Token: 5dda45b0-2b34-4d8c-8f52-1afd98cefd9e' \
  -H 'cache-control: no-cache'
```

**Create Item**
```
curl -X POST \
  http://localhost:5000/lists/%3Clist_id%3E/items \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: b34618da-a4db-44ad-a61b-cbcb71727ba7' \
  -H 'cache-control: no-cache' \
  -d '{
    "description": "Potatoes",
    "status": "incomplete"
}'
```

**Update Item**
```
curl -X PUT \
  http://localhost:5000/lists/%3Clist_id%3E/items/%3Citem_id%3E \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 434ea445-fa82-43e2-8282-8a1c35b383d0' \
  -H 'cache-control: no-cache' \
  -d '{
    "description": "New Potatoes",
    "status": "incomplete"
}'
```

**Delete Item**
```
curl -X DELETE \
  http://localhost:5000/lists/%3Clist_id%3E/items/%3Citem_id%3E \
  -H 'Postman-Token: c5e2ec0d-56a0-455d-9f08-32e5652c1a1d' \
  -H 'cache-control: no-cache'
```

## Known Limitations

* Limitation 1
* Limitation 2
* Limitation 3

## Built With

* [Flask](http://flask.pocoo.org/) - Python microframework
* [SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - Flask extension allowing for database connections

## Author

* **Steven Yerxa** - [syerxa](https://github.com/syerxa)
