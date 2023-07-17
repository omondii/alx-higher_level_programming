#!/usr/bin/python3
"""
Imported modules:
json
"""
import json


class Base:
    """
    This is the base class of of all other classes in this project
    base.py manages id attribute in all future classes.
    Params:
         private class attribute: __nb_objects
         id: increments according to the public attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the json rep of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        pass

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            data = json.loads(json_string)
            return data
