#!/usr/bin/python3
'''takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header'''
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    payload = {'email': argv[2]}
    req = requests.post(url, data=payload)
    print(req.text)
