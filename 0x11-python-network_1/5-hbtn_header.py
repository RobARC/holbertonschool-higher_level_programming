#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays
    the value of the variable X-Request-Id in the response header
"""

import requests
from sys import argv


def main(argv):
    """ method that take a url as argument and print like id """

    url = argv[1]
    response = requests.get(url)
    headers = response.headers.get('X-Request-Id')
    print(headers)


if __name__ == "__main__":
    main(argv)
