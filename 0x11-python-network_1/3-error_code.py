#!/usr/bin/python3
"""
Imported
urllib
sys
"""
import urllib.request
import sys


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
        print(data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
