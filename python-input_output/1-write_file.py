#!/usr/bin/python3
"""rtyui"""
def write_file(filename="", text=""):
    """741852963"""
    with open(filename, mode="w" , encoding="utf-8") as oo:
        oo.write(text)
        return len(text)
