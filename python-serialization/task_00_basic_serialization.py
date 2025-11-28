#!/usr/bin/python3
""" 7777998888 """

import json

def serialize_and_save_to_file(data, filename):
    """1133"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_and_deserialize(filename):
    """ ggg"""
    with open(filename, 'r', encoding='utf-8') as f:
         return json.load(f)
