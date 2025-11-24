#!/usr/bin/python3
"'classdi qaqa uzatma'"
class Rectangle:
    "'Defines class'"
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        "'uytre'"
        return self.__width
    
    @width.setter
    def width(self, value):
        "'Set width'"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """heigth"""
        return self.__height
    
    @height.setter
    def heigth(self, value1):
        if not isinstance(value1, int):
            raise TypeError("height must be an integer")
        if value1 < 0:
            raise ValueError("height must be >= 0")
        self.__height = value1
