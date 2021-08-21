#!/usr/bin/python3
"""Module: 0-hbtn_stattus.py:
    script that fetches https://intranet.hbtn.io/status"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("    - type:", type(html))
        print("    - content:", html)
        print("    - utf8 content:", html.decode("utf-8"))
