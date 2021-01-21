#!/usr/bin/python3
"""module save object to a file"""


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation:"""

    import json

    with open(filename, 'w', encoding='utf-8') as f:
        tojason = json.dumps(my_obj)
        return f.write(tojason)
