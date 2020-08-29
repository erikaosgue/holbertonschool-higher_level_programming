#!/usr/bin/python3
""" Script that fetches https://intranet.hbtn.io/status using package requests
Usage: ./4-hbtn_status.py """

import requests

if __name__ == "__main__":
    body = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(body.text)))
    print("\t- content: {}".format(body.text))
