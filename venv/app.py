from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Importing models
from models import db

db = SQLAlchemy
# Initializing the Flask app
app = Flask(__name__)
app.config.from_object('config.Config')
migrate = Migrate(app, db)