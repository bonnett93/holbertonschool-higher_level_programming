#!/usr/bin/python3
'''File: 6. load from json'''
import json


def load_from_json_file(filename):
    '''Creates an Object from a “JSON file'''
    with open(filename, "r+") as f:
        json.load(f)
