#!/usr/bin/python3
"""
Imported modules:
json
"""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file"
    Params:
       filename - file to use
    """
    with open(filename, "r") as file:
        """
        json.loads deserializes the json data into  a python object
        """
        data = json.load(file)
        return(data)
