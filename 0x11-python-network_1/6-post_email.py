#!/usr/bin/python3
""" Takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response.
Usage: ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    payload = {"email": sys.argv[2]}

    response = requests.post(url, data=payload)
    print(response.text)
