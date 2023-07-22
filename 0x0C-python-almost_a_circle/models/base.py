#!/usr/bin/python3
"""
Imported modules:
json
turtle - drawing module
"""
import json
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        pass

    @staticmethod
    def draw(list_rectangles, list_squares):
        window = turtle.Screen()
        window.title("Drawing from created instances")
        t = turtle.Turtle()

        for rect in  list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)

        for square in list_rectangles:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.width)
                t.left(90)

        t.hideturtle()
        window.mainloop()
