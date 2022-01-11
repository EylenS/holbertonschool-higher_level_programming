#!/usr/bin/python3
'''sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response ('''
from urllib.request import urlopen, Request
from urllib import parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    e_mail = {'email': argv[2]}
    encoded_args = parse.urlencode(e_mail).encode('utf-8')
    req = Request(url, encoded_args)
    with urlopen(req) as response:
        the_page = response.read()
    print(urlopen(url, encoded_args).read().decode('utf-8'))
