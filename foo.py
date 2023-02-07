#! /usr/bin/python
#-*-coding: utf-8 -*-
# 2023-02-07:
# 2022-12-21: 
# 2020-01-19: 
# calculates the area of squares, rectangles, or circles... and maybe triangles.

def square(L):
    return L * L

def rectangle(width , height):
    return width * height

def circle(radius):
    return 3.14159 * radius ** 2

def triangle(base , height):
    return base * height / 2
 
def options():
    print()
    print("Options:")
    print("s = calculate the area of a square.")
    print("c = calculate the area of a circle.")
    print("r = calculate the area of a rectangle.")
    print("t = calculate the area of a triangle.")
    print("q = quit")
    print()
 
print("This program will calculate the area of a square, circle or rectangle.")
choice = "x"
options()
while choice != "q":
    choice = input("Please enter your choice: ")
    if choice == "s":
        L = float(input("Length of square side: "))
        print("The area of this square is", square(L))
        options()
    elif choice == "c":
        radius = float(input("Radius of the circle: "))
        print("The area of the circle is", circle(radius))
        options()
    elif choice == "r":
        width = float(input("Width of the rectangle: "))
        height = float(input("Height of the rectangle: "))
        print("The area of the rectangle is", rectangle(width, height))
        options()
    elif choice == "t":
        base = float(input("Base of the triangle: "))
        height = float(input("Height of the triangle: "))
        print("The area of the triangle is", triangle(base, height))
        options()
    elif choice == "q":
        print(" ",end="")
    else:
        print("Unrecognized option.")
        options()
        
