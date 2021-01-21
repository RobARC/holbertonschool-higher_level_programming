#!/usr/bin/python3
"""module returns python object"""


def from_json_string(my_str):
    """function that returns python object string):"""

    import json

    topython = json.loads(my_str)
    return topython
