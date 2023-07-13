#!/usr/bin/python3
"""
No modules imported
"""


class Student():
    def __init__(self, first_name, last_name, age):
        """
        Initialize public attributes of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved.
        Otherwise, all attributes must be retrieved

        """
        if (attrs is None):
            return self.__dict__
        my_dict = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    my_dict[key] = value
        return my_dict

    def reload_from_json(sel, json):
        """that replaces all attributes of the Student instance"""
        for i, j in json.items():
            self.__dict__[i] = j
