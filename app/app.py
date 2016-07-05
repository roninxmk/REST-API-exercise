from flask import Flask
from db import Base, engine
from api import rule


app = Flask(__name__)


# Create Blueprints
app.register_blueprint(rule)


# Create tables
Base.metadata.create_all(engine)
