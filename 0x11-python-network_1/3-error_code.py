#!/usr/bin/python3

"""
Send request to url and display body of response
decoded in utf-8
"""
if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error as error

    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
