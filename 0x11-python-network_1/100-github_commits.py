#!/usr/bin/python3

"""
List all 10 commits of the repository `rails`
by user `rails`
Print all commits by `<sha>: <author name>`
"""

if __name__ == '__main__':
    import sys
    import requests

    url = 'https://api.github.com/repos/{}/{}/commits'\
        .format(sys.argv[1], sys.argv[2])
    params = {
        'per_page': 10
    }
    r = requests.get(url, params=params)
    res = r.json()
    for el in res:
        print('{}: {}'.format(
            el.get('sha'),
            el.get('author').get('login')
        ))
