#!/usr/bin/python3
"""Module: 7-error_code.py:
    script that takes in a URL, sends a request to the URL and
    displays the body of the response."""

if __name__ == '__main__':
    import requests
    import sys

    req = requests.get(sys.argv[1])
    status = req.status_code
    if status > 400:
        print('Error code:', status)
    else:
        print(req.text)
