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
    url = argv[1]
    email = {'email': argv[2]}

    email = urllib.parse.urlencode(email)
    email = email.encode('utf-8')

    # make request object
    request = urllib.request.Request(url, email)

    with urllib.request.urlopen(request) as response:
        response = response.read()
        response = response.decode('utf-8')
        print(response)
