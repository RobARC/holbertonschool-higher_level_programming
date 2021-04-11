#!/usr/bin/python3
""" script that takes in a URL and an email address, sends
    a POST request to the passed URL with the email as a
    parameter, and finally displays the body of the response.
"""

import requests
from sys import argv


def main(argv):
    url = argv[1]
    email = {'email': argv[2]}
    response = requests.post(url, data=email)
    print(response.text)


if __name__ == "__main__":
    main(argv)
