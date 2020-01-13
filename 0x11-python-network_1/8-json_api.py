#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
'''

import requests
import sys
if __name__ == '__main__':
    letter = ""
    if len(sys.argv) == 2:
        letter = sys.argv[1]

    post_data = {'q': letter}
    r = requests.post('http://0.0.0.0:5000/search_user', data=post_data)
    try:
        json_response = r.json()
        if not json_response:
            print('No result')
        else:
            print('[{}] {}'.format(json_response['id'], json_response['name']))
    except Exception as ex:
        print('Not a valid JSON')
