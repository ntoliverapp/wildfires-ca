from flask_sqlalchemy import SQLAlchemy
import wildfires_ca

from wildfires_ca.routes import main 

db = SQLAlchemy(wildfires_ca)