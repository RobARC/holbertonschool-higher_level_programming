#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of
    the response (decoded in utf-8)
"""

from urllib import request
from urllib.parse import urlencode
from sys import argv


def main(argv):
    """ method that take a url and an email as argument
    and print email adress
    """

    url = argv[1]
    email = {'email': argv[2]}
    data = urlencode(email)
    data = data.encode('utf8')
    req = request.Request(url, data)
    with request.urlopen(req) as r:
        response = r.read()
        print(response.decode('utf8'))


if __name__ == "__main__":
    main(argv)
