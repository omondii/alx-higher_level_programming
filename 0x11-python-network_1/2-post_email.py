#!/usr/bin/python3
"""
Imported modules
sys
urllib
parse
"""
import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data, method='POST')
    with urllib.request.urlopen(req) as response:
        post = response.read()
    print(data.decode('utf-8'))
