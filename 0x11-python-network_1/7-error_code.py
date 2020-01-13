#!/usr/bin/python3
'''
Write a Python script that takes in a URL
sends a request to the URL and displays the body of the response.
'''

import requests
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    status_code = r.status_code
    if status_code >= 400:
        print('Error code: {}'.format(status_code))
    else:
        print(r.text)
