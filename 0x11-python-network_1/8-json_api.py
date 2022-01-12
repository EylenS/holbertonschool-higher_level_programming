#!/usr/bin/python3
'''takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q. If no argument is given, set q=""'''
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ''
        r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
        try:
            req = r.json()
            id = req.get('id')
            name = req.get('name')
            if len(r.json) == 0:
                print('No result')
            else:
                print('[{}] {}'.format(id, name))
        except:
            print('Not a valid JSON')
