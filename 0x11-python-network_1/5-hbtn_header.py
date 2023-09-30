#!/usr/bin/python3
"""
Imported modules
requests
sys
"""
import requests
import sys

if __name__ == "__main__":
    try:
        with requests.get(sys.argv[1]) as response:
            response.raise_for_status()
            print(response.headers.get('X-Request-Id'))
    except requests.exceptions.RequestException as e:
        print('Error', e)
