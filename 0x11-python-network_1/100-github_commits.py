#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest) of the repository “rails”
by the user “rails”
Usage: ./100-github_commits.py rails rails"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[1], sys.argv[2])

    response = requests.get(url)
    list_of_dict = response.json()

    try:
        for i in range(10):
            print("{} {}".format(list_of_dict[i].get(
                "sha"), list_of_dict[i].get("commit").get("author").get("name")))
    except:
        pass
