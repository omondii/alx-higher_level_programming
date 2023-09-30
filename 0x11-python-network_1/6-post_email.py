#!/usr/python3
"""
Imported modules;
requests
sys
"""
import requests
import sys

if __name__ = '__main__':
    email = sys.argv[2]
    url = sys.argv[1]
    data = {'email': email}
    try:
        with requests.post(url, data) as response:
            response.raise_for_status()
            html = response.text
        print(html)
    except requests.exceptions.RequestException as e:
        print('Error:', e)
