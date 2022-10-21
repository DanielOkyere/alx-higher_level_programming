#!/usr/bin/python3

"""
script authenticates Github Api
"""

if __name__ == '__main__':
    import sys
    import requests

    github_url = 'https://api.github.com/user'
    params = {
        'username': sys.argv[1],
    }
    h = {
        'Authorization': 'Bearer ' + sys.argv[2]
    }
    r = requests.get(github_url, params=params, headers=h)
    print(r.json().get('id'))
