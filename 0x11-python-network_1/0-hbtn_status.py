#!/usr/bin/python3
'''
write a Python script that fetches https://intranet.hbtn.io/status
'''
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    resp = response.read()
    headers = response.info()
    print('Body response:')
    print('\t- type: {}'.format(type(resp)))
    print('\t- content: {}'.format(resp))
    print('\t- utf8 content: {}'.format(resp.decode('utf-8')))
