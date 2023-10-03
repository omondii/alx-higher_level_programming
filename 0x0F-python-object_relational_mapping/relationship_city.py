#!/usr/bin/python3
""" Define state model """
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """ Define class state to create link to db """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, autoincrement=True,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
