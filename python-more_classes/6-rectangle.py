#!/usr/bin/python3
"""Module that defines a Rectangle class that counts its instances."""


class Rectangle:
    """A class that defines a rectangle by its width and height.

    Attributes:
        number_of_instances: number of Rectangle instances currently alive.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
            width: the width of the rectangle (integer >= 0).
            height: the height of the rectangle (integer >= 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        If width or height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle printed with the character #.

        If width or height is 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        row = "#" * self.__width
        return "\n".join([row] * self.__height)

    def __repr__(self):
        """Return a string that can recreate the rectangle with eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and decrement the counter on deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
