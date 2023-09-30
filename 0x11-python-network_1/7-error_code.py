#!/usr/bin/python3
"""
Imported modules;
requests
sys
"""
import requests
import sys


if __name__ == '__main':
    utl = sys.argv[1]
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            html = response.text
        print(html)
    except requests.exceptions.RequestException as e:
        if hasattr(e.response, 'status_code'):
            print('Error code:', e.response.status_code)
        else:
            print('Error Code:', e)
