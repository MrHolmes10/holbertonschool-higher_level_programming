#!/usr/bin/python3
"""CSV data to json"""
    
import csv
import json

def convert_csv_to_json(csv_filename):
    """ convert csv to json"""
    try:
        # csv data
        with open(csv_filename, 'r', encoding='utf-8') as cs_file:
            reader = csv.DictReader(cs_file)
            data = list(reader)
        
        # write json
        with open('data.json', 'w', encoding='uf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        return True

    except FileNotFoundError:
        # csv file
        return False
    except Exception:
        # Any
        return False
