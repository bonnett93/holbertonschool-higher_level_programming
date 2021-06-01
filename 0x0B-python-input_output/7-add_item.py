#!/usr/bin/python3
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_file = load_from_json_file("add_item.json")
save_to_json_file(argv, my_file)
