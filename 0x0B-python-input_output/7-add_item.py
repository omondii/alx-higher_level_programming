#!/usr/bin/python3
"""
Imported modules:
json, sys
save_to_json_file, load_from_json_file
"""
from json import JSONDecodeError
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []
try:
    my_list = list(load_from_json_file("add_item.json"))
except FileNotFoundError:
    pass

for arg in range(1, len(argv)):
    my_list.append(argv[arg])

save_to_json_file(my_list, "add_item.json")
