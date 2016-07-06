from flask import Flask
from db import Base, engine
from api import rule, event, user


app = Flask(__name__)


# Create Blueprints
app.register_blueprint(rule)
app.register_blueprint(event)
app.register_blueprint(user)

# Create tables
Base.metadata.create_all(engine)
