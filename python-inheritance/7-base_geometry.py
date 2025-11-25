#!/usr/bin/python3
"""7777"""

class BaseGeometry():
    """i am the best"""
    
    
    def area(self):
         """fff"""
    
         raise Exception("area() is not implemented")
     
    
    
    def integer_validator(self, name, value):
         """rtrt"""
    
         if type(value) != int :
            raise TypeError("{} must be an integer".format(name))
         if value <= 0 :
            raise ValueError("{} must be greater than 0".format(name))
