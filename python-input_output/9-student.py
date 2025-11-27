#!/usr/bin/python3
"""755qwert"""

class student:
    """class for unknown reason """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """8 deki funcsiya"""
        return self.__dict__
