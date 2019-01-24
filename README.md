# DH Demo App - ToDo List API

This project is a technical Demo App of a ToDo List JSON API using Flask and SQLAlchemy.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Clone the Project

Clone the project to your local machine
```
git clone https://github.com/syerxa/DH-Demo-App.git
```


### Prerequisites

The following steps are needed to successfully run the app on your local machine.

Create an environment in your project folder
```
python3 -m venv venv
. venv/bin/activate
```
or on Windows
```
py -3 -m venv venv
venv\Scripts\activate
```

Install the following in your created environment
```
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Caching
pip install PyMySQL
pip install pytest
pip install flask_testing
```


### Installing the Project

Edit line 13 of app/\_\_init__.py to point to your local MySQL database.

```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@localhost/<database>'
```

Run the migration.py script to create the tables and seed data in your database.

```
python3 migration.py
```

Finally, start flask from the root directory.

```
FLASK_APP=main.py flask run
```


## Running the Tests

The unit tests can be run from the root directory.

```
pytest
```


## API Calls

You can use the included Postman collection or the cURL commands below to access the API endpoints.

**Get All Lists**
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

**Get All Items from List**
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

* Update List does not support the inclusion of Items.  Items can be updated via the /lists/<list_id>/items/<item_id> endpoint.
* Attribute fields only have basic validation, which includes required attribute check and valid status attribute value.


## Built With

* [Flask](http://flask.pocoo.org/) - Python microframework
* [SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - Flask extension allowing for database connections
* [Flask Caching](https://pythonhosted.org/Flask-Caching/) - Flask extension allowing for backend caching
* [PyMySQL](https://pymysql.readthedocs.io/en/latest/) - Python MySQL support
* [PyTest](https://docs.pytest.org/en/latest/) - Python testing framework
* [Flask Testing](https://pythonhosted.org/Flask-Testing/) - Flask extension allowing for unit testing utilities


## Author

* **Steven Yerxa** - [syerxa](https://github.com/syerxa)
