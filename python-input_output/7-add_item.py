#!/usr/bin/python3
"""123456"""
import os, sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
# if condition
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# add comand
items.extend(sys.argv[1:])

# save

save_to_json_file(items, filename)
