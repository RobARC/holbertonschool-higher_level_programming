#!/usr/bin/python3
"""  script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv


def main(argv):
    """  script that takes in a letter and sends a POST request to
        http://0.0.0.0:5000/search_user with the letter as a paramete
    """

    url = 'http://f1859af609d9.b380b380.hbtn-cod.io:5000/search_user'

    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    payload = {'q': q}
    req = requests.post(url, data=payload)
    try:
        response = req.json()
        if bool(response):
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
    except:
            print("Not a valid JSON")


if __name__ == "__main__":
    main(argv)
