#!/usr/bin/python3
'''
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of the response
(decoded in utf-8).
'''

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        url = sys.argv[1]
        try:
            with urllib.request.urlopen(url) as response:
                resp = response.read()
                print(resp.decode('utf-8'))

        except urllib.error.HTTPError as error:
            print('Error code: {}'.format(error.code))
