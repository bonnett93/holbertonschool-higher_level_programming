#!/usr/bin/python3
"""Module: 5-hbtn_header.py:
    script that takes in a URL, sends a request to the URL and displays
    the value of the variable X-Request-Id in the response header"""

if __name__ == '__main__':
    import requests
    import sys

    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
