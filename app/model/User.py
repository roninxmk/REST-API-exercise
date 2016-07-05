from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Rule import association_table
from ..db import Base


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False)

    rules = relationship(
        'Rule', secondary=association_table)
