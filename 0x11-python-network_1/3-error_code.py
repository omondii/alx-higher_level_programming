#!/usr/bin/python3
"""
Imported
urllib
sys
"""
import urllib.request
import sys


if __name__ == '__main__':
    """
    Python script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
    manage urllib.error.HTTPError exceptions and print: Error code:
    followed by the HTTP status code
    Params:
      req - request instance, contains the body of the request
      data - instance that stores the contents of the received response
    """
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
        print(data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
