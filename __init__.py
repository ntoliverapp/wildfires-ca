import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))


# def create_app(config_file='config.py'):
    
#     app = Flask(__name__)
#     app.config.from_pyfile(config_file)
#     db = SQLAlchemy(app)

#     db.init_app(app)
#     return app

