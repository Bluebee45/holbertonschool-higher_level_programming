#!/usr/bin/python3
"""
5. Detect instance deletion
Add __rdel__ method
"""


class Rectangle:
    """
    Class Square

    Attributes:
        __width
        __height

    Methods:
        def area(self)
        def perimeter(self)
        def __str__(self)
        def __repr__(self)
        def __del__(sself)
    """
    def __init__(self, width=0, height=0):
        """
        Initializes square
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        Returns a string with # rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        string = ""
        for i in range(0, self.__height):
            string += "#" * self.__width
            if i < self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """
        Return a string representation of the rectangle
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Destructor
        """
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle are
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Returns the rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))
