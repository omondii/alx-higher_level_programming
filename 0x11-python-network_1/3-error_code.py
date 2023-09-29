#!/usr/bin/python3
"""
Imported
urllib
sys
"""
import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
