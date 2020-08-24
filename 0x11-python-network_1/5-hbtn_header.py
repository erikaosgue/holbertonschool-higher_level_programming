#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header. Using requests package
Usage: ./5-hbtn_header.py https://intranet.hbtn.io """

import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
