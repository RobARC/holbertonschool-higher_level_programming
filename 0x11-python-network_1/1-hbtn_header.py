#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header
    of the response.
"""

from urllib import request
from sys import argv


def main(argv):
    """ method that take a url as argument and print like id """

    url = argv
    with r.equest.urlopen(url) as r:
        headers = r.info()
        print(headers['X-Request-Id'])


if __name__ == "__main__":
    main(argv[1])
