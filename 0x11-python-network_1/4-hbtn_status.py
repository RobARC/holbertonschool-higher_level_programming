#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status using package
    request
"""


from requests import get


def main():
    url = 'https://intranet.hbtn.io/status'
    response = get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
