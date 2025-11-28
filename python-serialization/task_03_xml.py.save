#!/usr/bin/env python3
""" tasks 3 seri"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ rrr"""
    root = ET.Element("data")
    
    # add 
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    # XMl
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text  # Keep as string
        return data
    except Exception:
        # Return empty dict if file not found or malformed
        return {}
