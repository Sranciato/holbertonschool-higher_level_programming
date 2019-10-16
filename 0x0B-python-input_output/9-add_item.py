#!/usr/bin/python3
"""add args to a python list"""

import json
import os.path
from sys import argv

save_to = __import__('7-save_to_json_file').save_to_json_file
load_from = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    li = []
    if os.path.exists("add_item.json"):
        li = load_from("add_item.json")
    li.append(argv[1:])
    save_to(li, "add_item.json")
