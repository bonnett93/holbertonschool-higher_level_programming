#!/usr/bin/python3
"""Module: 10-my_github.py:
    script that takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id"""

if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    token = sys.argv[2]
    headers = {'Authorization': 'token ' + token}
    url = 'https://api.github.com/user'

    req = requests.post(url, auth=(username, token))
    try:
        print(req.json()['id'])
    except:
        print('None')
