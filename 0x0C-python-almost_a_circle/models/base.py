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
        """ returns .json with the string represents of list_objs """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dictList = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(dictList)
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ Returns .json file that reps a list of dicts"""
        if json_string is None:
            return []
        else:
            data = json.loads(json_string)
            return data

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            r = cls(4)
        else:
            r = cls(4, 4)

        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r") as f:
                jsonList = f.read()
                dictList = cls.from_json_string(jsonList)
                objList = [cls.create(**obj) for obj in dictList]

                return objList
        except FileNotFoundError:
            return []
