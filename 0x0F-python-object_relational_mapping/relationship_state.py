#!/usr/bin/python3
""" state model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ class state to be linked to db table """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)

    name = Column(String(123), nullable=False)

    cities = relationship('City', cascade='all, delete', backref='state')
