#!/usr/bin/python3
"""Takes in a letter and sends a POST reque. to http://0.0.0.0:5000/search_user
with the letter as a parameter.
Usage: ./8-json_api.py <letter>"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    letter = "" if len(sys.argv) <= 1 else sys.argv[1]
    payload = {"q": letter}

    response = requests.post(url, data=payload)
    try:
        r = response.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except:
        print("Not a valid JSON")
