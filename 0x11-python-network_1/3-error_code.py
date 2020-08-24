#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8).
Usage: ./3-error_code.py http://0.0.0.0:5000 """


import urllib.request
import urllib.error
import sys

import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = urllib.request.urlopen(url)
        print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
