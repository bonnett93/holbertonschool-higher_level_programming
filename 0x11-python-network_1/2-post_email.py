#!/usr/bin/python3
"""Module: 2-post_email.py:
     takes in a URL and an email, sends a POST request to the passed URL
     with the email as a parameter, and displays the body of the response
     (decoded in utf-8)"""

if __name__ == '__main__':
     import urllib.request
     import urllib.parse
     import sys

     data = urllib.parse.urlencode({'email': sys.argv[2]})
     data = data.encode('ascii')
     url = sys.argv[1]
     with urllib.request.urlopen(url, data) as response:
     print(response.read().decode('utf-8'))
