#!/usr/bin/python3
'''takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q. If no argument is given, set q=""'''
import json
import requests
from sys import argv


if __name__ == "__main__":
    try:
        payload = {'q': argv[1]}
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        if r.headers.get('content-type') != 'application/json':
            raise TypeError
        req = r.json()
        if req:
            id = req.get('id')
            name = req.get('name')
            print('[{}] {}'.format(id, name))
        elif len(req) == 0:
            print('No result')
    except IndexError:
        print('No result')
    except TypeError:
        print('Not a valid JSON')
