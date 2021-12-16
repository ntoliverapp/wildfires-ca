from flask import Flask 
from .commands import create_tables
from .extensions import db
from .models import Wildfire
from .routes.main import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)


    app.register_blueprint(main)


    return app

# def create_app(config_file='config.py'):
    
#     app = Flask(__name__)
#     app.config.from_pyfile(config_file)
#     db = SQLAlchemy(app)

#     db.init_app(app)
#     return app

