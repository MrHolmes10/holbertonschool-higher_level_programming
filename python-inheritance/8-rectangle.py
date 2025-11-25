#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry validation.
    Width and height are private and validated as positive integers.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle after validating width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: if width or height is not an integer.
            ValueError: if width or height is <= 0.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
