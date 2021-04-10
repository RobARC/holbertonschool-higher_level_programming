#!/usr/bin/python3
""" Script that fetches https://intranet.hbtn.io/status """


from urllib import request


def main():
    """ method to print a response of a specific url """

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        body_response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_response)))
        print("\t- content: {}".format(body_response))
        print("\t- utf8 content: {}".format(body_response.decode('utf-8')))

if __name__ == "__main__":
    main()
