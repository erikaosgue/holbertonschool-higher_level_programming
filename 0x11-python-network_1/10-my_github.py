#!/usr/bin/python3
"""Takes your Github credentials (username and password) and uses the Github
API to display your id
Usage: ./10-my_github.py <username> <password>"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]
    login = requests.get(url, auth=HTTPBasicAuth(username, token))
    print(login.json().get("id"))
