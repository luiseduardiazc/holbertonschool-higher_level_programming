#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
'''

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        post_data = urllib.parse.urlencode({'email': email}).encode()
        with urllib.request.urlopen(url, post_data) as response:
            resp = response.read()
            print(resp.decode('utf-8'))
