#!/usr/bin/python3
"""
Imported modules
requests module
"""
import requests


"""
4-hbtn_status.py is a vaariation of 1-hbtn_header.py in that it uses the
requests module. It also handles errors and exceptions
Params:
  url - link to bee fetched
  req - the http request being made
"""
url = 'https://alx-intranet.hbtn.io/status'
try:
    with requests.get(url) as response:
        response.raise_for_status()
        html = response.text
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
except requests.exceptions.RequestException as e:
    print('Error:', e)
