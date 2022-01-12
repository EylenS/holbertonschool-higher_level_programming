#!/usr/bin/python3
'''Takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8)'''
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            html = response.read()
        print(html.decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
