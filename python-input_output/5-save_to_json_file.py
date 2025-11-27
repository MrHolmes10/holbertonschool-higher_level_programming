#!/usr/bin/python3
"""@ssfdd"""
import json


def save_to_json_file(my_obj, filename):
    """234567"""
    with open(filename, mode ="w", encoding="utf-8" ) as oo:
         json.dump(my_obj, oo)
