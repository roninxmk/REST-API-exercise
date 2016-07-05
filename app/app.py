from flask import Flask
from db import Base, engine

app = Flask(__name__)

# Create tables
Base.metadata.create_all(engine)


@app.route('/')
def hello_world():
    return "Hello World!"
