#!/usr/bin/python3
"""
Takes a URL, sends a request and display `X-Request-Id`
"""

if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
