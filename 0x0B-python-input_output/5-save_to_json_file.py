#!/usr/bin/python3
"""
imported modules:
json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file, using a JSON representation
    params:
      my_obj: data to write into file
      filename: file to write into
    """
    with open(filename, "w") as file:
        """
        json.dump serializes my_obj into a json formatted string and writes to
        the file.
        """
        json.dump(my_obj, file)
