#!/usr/bin/python3
"""
Imported modules
declarative_base from sqlalchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


""" Create a directive base """
Base = declarative_base()

        """
        State class definition
        Params:
           id: id field ogf the class
           name: state name
        """
class State(Base):

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
