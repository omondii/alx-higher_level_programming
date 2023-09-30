#!/usr/bin/python3
"""
Imported modules
sys
requests
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    auth = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get('https://api.github.com/user', auth=auth)

    print(req.json().get('id'))
