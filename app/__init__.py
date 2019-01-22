from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
    
db = SQLAlchemy()
cache = Cache(config={'CACHE_TYPE': 'simple'})

def create_app():
    app = Flask(__name__)
    # Edit following line to configure the location of your mysql db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:2Federate@localhost/dhdemo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    cache.init_app(app)
    return app
