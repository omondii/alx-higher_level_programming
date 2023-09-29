#!/usr/bin/python3
"""
Imported modules
urllib
sys
"""
import urllib.request
import sys


if '__name__' == '__main__':
    """
    Python script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
    Params:
       req - make an http request based on url(1st arg passed)
       with - open the result of the made request as the http response
    Prints the value X-requested-id from the header of the openned url
    """
    req = urllib.requests.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
