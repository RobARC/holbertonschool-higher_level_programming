#!/usr/bin/python3
"""module returns JSON representation"""


def to_json_string(my_obj):
    """unction that returns the JSON representation
    of an object (string):"""

    import json

    tojson = json.dumps(my_obj)
    return tojson
