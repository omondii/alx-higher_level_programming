#!/usr/bin/python3
"""
json module import
"""
import json


def from_json_string(my_str):
    """
    function to that returns an object represented by a json string
     Params:
         my_string - json string to convert back
    """
    data = json.loads(my_str)
    return (data)
