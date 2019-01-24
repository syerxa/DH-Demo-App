# DH Demo App - ToDo List API

This project is a technical Demo App of a simple ToDo List JSON API using Flask and SQLAlchemy.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The following are needed in order to successfully run the app on your local machine

Create an environment
```
python3 -m venv venv
. venv/bin/activate
```
or on Windows
```
py -3 -m venv venv
venv\Scripts\activate
```

Install the following in your environment
```
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Caching
pip install PyMySQL
pip install pytest
pip install flask_testing
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
  -H 'cache-control: no-cache'
```

**Get List**
```
curl -X GET \
  http://localhost:5000/lists/<list_id> \
  -H 'cache-control: no-cache'
```

**Create List**
```
curl -X POST \
  http://localhost:5000/lists \
  -H 'Content-Type: application/json' \
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
  http://localhost:5000/lists/<list_id> \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"description": "My Todo List Updated",
	"title": "TODO Updated"
}'
```

**Delete List**
```
curl -X DELETE \
  http://localhost:5000/lists/<list_id> \
  -H 'cache-control: no-cache'
```

**Get Items from List**
```
curl -X GET \
  http://localhost:5000/lists/<list_id>/items \
  -H 'cache-control: no-cache'
```

**Get Item**
```
curl -X GET \
  http://localhost:5000/lists/<list_id>/items/<item_id> \
  -H 'cache-control: no-cache'
```

**Create Item**
```
curl -X POST \
  http://localhost:5000/lists/<list_id>/items \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
    "description": "Potatoes",
    "status": "incomplete"
}'
```

**Update Item**
```
curl -X PUT \
  http://localhost:5000/lists/<list_id>/items/<item_id> \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
    "description": "New Potatoes",
    "status": "incomplete"
}'
```

**Delete Item**
```
curl -X DELETE \
  http://localhost:5000/lists/<list_id>/items/<item_id> \
  -H 'cache-control: no-cache'
```

## Known Limitations

* Limitation 1
* Limitation 2
* Limitation 3

## Built With

* [Flask](http://flask.pocoo.org/) - Python microframework
* [SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - Flask extension allowing for database connections
* [Flask Caching](https://pythonhosted.org/Flask-Caching/) - Flask extension allowing for backend caching
* [PyMySQL](https://pymysql.readthedocs.io/en/latest/) - Python MySQL support
* [PyTest](https://docs.pytest.org/en/latest/) - Python testing framework
* [Flask Testing](https://pythonhosted.org/Flask-Testing/) - Flask extension allowing for unit testing utilities

## Author

* **Steven Yerxa** - [syerxa](https://github.com/syerxa)
