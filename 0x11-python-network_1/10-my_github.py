#!/usr/bin/python3
""" script that takes your GitHub credentials (username and
    password) and uses the GitHub API to display your id
"""


import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):

    user = argv[1]
    passw = argv[2]

    r = requests.get('https://api.github.com/user',
                     auth=HTTPBasicAuth(user, passw))

    try:
        info = r.json()
        print(info['id'])
    except:
        print('None')


if __name__ == "__main__":
    main(argv)
