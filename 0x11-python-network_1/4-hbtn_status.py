#!/usr/bin/python3
"""
Script fetches status
Uses the request module
"""

if __name__ == "__main__":
    import sys
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
