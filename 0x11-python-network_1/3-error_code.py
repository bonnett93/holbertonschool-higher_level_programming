#!/usr/bin/python3
"""Module: 3-error_code.py:
    takes in a URL, sends a request to the URL and displays the body
    of the response (decoded in utf-8).
    manage urllib.error.HTTPError exceptions and print:
        'Error code:' followed by the HTTP status code"""

if __name__ == '__main__':
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
