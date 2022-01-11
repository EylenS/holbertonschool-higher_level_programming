#!/usr/bin/python3
"""This module fetches an URL"""
from urllib.request import urlopen


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type:'.type(html))
        print('\t- content:', html)
        print('\t- utf8 content:', (html.decode('utf-8')))
