#!/usr/bin/python3
'''Fetches https://intranet.hbtn.io/status'''
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = requests.get(url)
    r = req.text
    print('Body response:')
    print('\t- type:', type(r))
    print('\t- content:', r)
