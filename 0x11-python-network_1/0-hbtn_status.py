#!/usr/bin/python3
"""
Imported modules
urllib - url fetching module
"""
import urllib.request


"""
Params:
  url - link to bee fetched
  req - the http request being made
"""
url = 'https://alx-intranet.hbtn.io/status'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'. format(html.decode('utf-8')))
