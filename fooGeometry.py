#! /usr/bin/python
#-*-coding: utf-8 -*-
# 2023-02-07: played w github's pylint action/workflow... not impressed.
# 2022-12-21:
# 2020-01-19:
# calculates the area of squares, rectangles, or circles... and maybe triangles.

# calculates the area of squares
def square(length):
    return length * length

# calculates the area of rectangles
def rectangle(width , height):
    return width * height

# calculates the area of circles.
def circle(radius):
    return 3.14159 * radius ** 2

# calculates the area of... maybe triangles.
def triangle(base , height):
    return base * height / 2

# present choices to user
def options():
    print()
    print("Options:")
    print("s = calculate the area of a square.")
    print("c = calculate the area of a circle.")
    print("r = calculate the area of a rectangle.")
    print("t = calculate the area of a triangle.")
    print("q = quit")
    print()
    
# do stuff
print("This program will calculate the area of a square, circle or rectangle.")
Choice = "x"
options()
while Choice != "q":
    Choice = input("Please enter your choice: ")
    if Choice == "s":
        length = float(input("Length of square side: "))
        print("The area of this square is", square(length))
        options()
    elif Choice == "c":
        radius = float(input("Radius of the circle: "))
        print("The area of the circle is", circle(radius))
        options()
    elif Choice == "r":
        width = float(input("Width of the rectangle: "))
        height = float(input("Height of the rectangle: "))
        print("The area of the rectangle is", rectangle(width, height))
        options()
    elif Choice == "t":
        base = float(input("Base of the triangle: "))
        height = float(input("Height of the triangle: "))
        print("The area of the triangle is", triangle(base, height))
        options()
    elif Choice == "q":
        print(" ",end="")
    else:
        print("Unrecognized option.")
        options()
