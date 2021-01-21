#!/usr/bin/python3
"""module create an object from jaso file"""


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”:"""

    import json

    with open(filename, 'r') as f:
        fromjson = f.read()
        return json.loads(fromjson)
