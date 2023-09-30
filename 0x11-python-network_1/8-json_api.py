#!/usr/bin/python3
"""
Imported modules;
requests
sys
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = '' if len(argv) == 1 else argv[1]
    data = {'q': q}
    req = requests.post(url, data)

    try:
        response = req.json()
        if response == {}:
            print('No result')
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print('Not a valid JSON')
