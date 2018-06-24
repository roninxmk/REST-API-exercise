from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import func
from app.db import Base



class Event(Base):

    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    timestamp = Column(TIMESTAMP, server_default=func.now())
    rule_id = Column(Integer, ForeignKey('rule.id'))

    rule = relationship('Rule')
