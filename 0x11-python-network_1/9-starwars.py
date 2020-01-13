#!/usr/bin/python3
'''
Write a Python script that takes in a string
and sends a search request to the Star Wars API
'''

import requests
import sys
if __name__ == '__main__':
    search = sys.argv[1]
    r = requests.get('https://swapi.co/api/people/?search=' + search)
    json_response = r.json()
    results = json_response['results']
    print("Number of results: {}".format(json_response['count']))
    for item in results:
        print(item['name'])
