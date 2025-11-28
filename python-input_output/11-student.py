#!/usr/bin/python3
"""tasks 11"""



class Student:
    """ class"""
    def __init__(self, first_name, last_name, age):
         """you tube"""

         self.first_name = first_name
         self.last_name = last_name
         self.age = age

    def to_json(self, attrs=None):
         """if att """

         if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            result = {}
            for key in attrs:
                if hasattr(self, key):
                    result[key] = getattr(self, key)
            return result

         return self.__dict__
   
    def reload_from_json(self, json):
        """123456789"""
        for i, j in json.items() :
            self.__dict__[i] = j
