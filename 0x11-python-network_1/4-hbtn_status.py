#!/usr/bin/python3
"""Module: 4-hbtn_status.py:
    script that fetches https://intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests

    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)
