#!/usr/bin/python3
"""Module: 8-json_api.py:
    takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) < 2:
        print('No result')
    q = sys.argv[1]
    payload = {'email': sys.argv[1]}
    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data=payload)
    try:
        res = req.json()
        if res:
            print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
