#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print(my_square)
print(my_square.area())
print(repr(my_square))
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
