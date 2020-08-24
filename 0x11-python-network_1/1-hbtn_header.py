#!/usr/bin/python3
"""  takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
Usage: ./1-hbtn_header.py https://intranet.hbtn.io"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get("X-Request-Id"))
