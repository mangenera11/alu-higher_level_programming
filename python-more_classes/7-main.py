#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

print("--")

Rectangle.print_symbol = "&"
print(my_rectangle_1)

print("--")

my_rectangle_2 = Rectangle(2, 3)
print(my_rectangle_2)

print("--")

my_rectangle_2.print_symbol = "C"
print(my_rectangle_2)
print(my_rectangle_1)
