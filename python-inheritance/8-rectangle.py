#!/usr/bin/python3
"""7777"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """i am the best"""
    
    def __init__(self, width, height):
        """123456"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("width", width)
        self.__height = height
