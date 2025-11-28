#!/usr/bin/python3
""" ffff """

import pickle
 class CustomObject:
     def __init__(self, name, age, is_student):
         self.name = name
         self.age = age
	 self.is_student = is_student

     def display(self):
         """777 """
         print(f"Name: {self.name}")
         print(f"Age: {self.age}")
         print(f"Is Student: {self.is_student}")

     def serialize(self, filename):
         """ fdff"""
         try:
             with open(filename, 'wb') as f:
                 pickle.dump(self, f)
         except Exception: 
             # weer
             return None

     @classmethod
     def deserialize(cls, filename):
         """777 """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            # Return None if file doesn't exist or deserialization fails
            return None
