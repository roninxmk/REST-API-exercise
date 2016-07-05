from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base


association_table = Table('user_alert', Base.metadata,
                          Column('user_id', Integer, ForeignKey('user.id')),
                          Column('rule_id', Integer, ForeignKey('rule.id')))


class Rule(Base):

    __tablename__ = 'rule'

    id = Column(Integer, primary_key=True)
    parameter = Column(String(32), nullable=False)
    threshold = Column(Integer, nullable=False)

    users = relationship('Rule', secondary=association_table)
    events = relationship('Event')
