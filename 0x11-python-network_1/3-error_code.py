#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""

from urllib import request
from urllib.error import HTTPError
from sys import argv


def main(argv):
    """ method to get http errors """

    url = argv[1]

    try:
        with request.urlopen(url) as r:
            response = r.read()
            print(response.decode('utf8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))


if __name__ == "__main__":
    main(argv)
