#!/usr/bin/python3
"""
Takes an email and send Post Request with email as a parameter
decoded in UTF-8
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    data = urllib.parse.urlencode({
        'email' : sys.argv[2]
    }).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
        print(data)