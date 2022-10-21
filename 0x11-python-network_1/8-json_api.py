#!/usr/bin/python3

"""
Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
"""

if __name__ == "__main__":
    import sys
    import requests

    try:
        q = "" if len(sys.argv) == 1 else sys.argv[1]
        url = 'http://0.0.0.0:5000/search_user'
        data = {'q': q}
        r = requests.post(url, data=data)
        res = r.json()

        if res == {}:
            print('No result')
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except valueError:
        print('Not a valid JSON')
