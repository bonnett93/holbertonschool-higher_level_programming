#!/usr/bin/python3
"""Module: 100-github_commits.py:
    List 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails”"""

if __name__ == '__main__':
    import requests
    import sys

    repo_name = sys.argv[1]
    owner = sys.argv[2]
    header = {'accept': 'application/vnd.github.v3+json', 'per_page':'1'}
    full_url = 'https://api.github.com/repos/{}/{}/commits'.format(owner,repo_name)
    print(full_url)
    req = requests.get(full_url)
    try:
        i = 0
        print(len(req.text))
        #for each in req.text:
        #    print(each, end="")
        #    i += 1
        #    if i == 100:
        #        break
    except:
        print('Fallo')
