#!/usr/bin/python3
'''
Write a Python script that takes in a URL,
sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
'''

import urllib.request
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            resp = response.read()
            headers = response.info()
            print(headers.__getitem__('X-Request-Id'))
