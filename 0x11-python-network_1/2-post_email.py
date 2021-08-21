#!/usr/bin/python3
"""Module: 1-hbtn_header.py:
    takes in a URL, sends a request to the URL and displays the value of
    the X-Request-Id variable found in the header of the response"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    url = sys.argv[1]
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
