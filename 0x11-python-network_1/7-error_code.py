#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the body of the
response.'''
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    r = req.status_code
    if r >= 400:
        print('Error code: {}'.format(r))
    else:
        print(req.text)
