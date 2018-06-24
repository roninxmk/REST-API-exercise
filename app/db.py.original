from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://exercise:Exercise123.@localhost:3306/rest_exercise'

Base = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()
