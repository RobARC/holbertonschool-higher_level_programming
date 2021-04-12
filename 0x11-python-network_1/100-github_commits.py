#!/usr/bin/python3
"""  script that takes 2 arguments in order to solve this
    challenge.
    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You dont need to check arguments passed to the script (number or type)
"""

import requests
from requests import get
from sys import argv


def main(argv):

    repo_name = argv[1]
    owner_name = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits?". \
          format(owner_name, repo_name)

    r = get(url)

    commits = r.json()

    for commit in commits[:10]:
        print(commit['sha'], end=": ")
        print(commit['commit']['author']['name'])


if __name__ == "__main__":
    main(argv)
