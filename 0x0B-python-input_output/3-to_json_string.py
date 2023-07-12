#!/usr/bin/python3
"""
json module - for data interchange
"""
import json
"""
json module - for data interchange
"""
def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object
    json_dump - takes python ds as input and returns a string
    representing the json data
    """
    json_string = json.dumps(my_obj)
    return (json_string)
