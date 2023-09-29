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
    """
    Python script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
    Params:
      email - email address
      values - dict that reps the data to post
      data - values is converted to a URL-encoded string
      req - instannce to make an http POST.
         it takes as args; a url,body of the POST request & the request method
    """
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data, method='POST')
    with urllib.request.urlopen(req) as response:
        post = response.read()
    print(data.decode('utf-8'))
