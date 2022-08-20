# Author: S. Muhammad Ali
# Date: Fall 2022 semester
# Course: CS 101 Programming Fundamentals
# Purpose: Drawing filled polygons using python's turtle library
# Reference: https://docs.python.org/3/library/turtle.html
# Functions:
#   - polygon: draws polygon using for loop.
#   - polygon_2: draws polygon using while loop.
# Concepts: the implementation below uses
#   - Usage of 'turtle', a built in library
#   - functions
#   - modular arithmetic
#   - iteration
#   - variables
# Variations:
#   - The code demonstrates how for loop can be used in place of while loops.
#   - The polygon can also be drawn without using any loops

from turtle import *  # imports all functions from the Turtle library/module


def polygon(sides, sides_length):
    ''' Creates a polygon of sides n with each side of length sides_length using for loops'''

    # initializing the screen and the pen with minimal settings
    my_screen = Screen()
    my_screen.title('my Drawing')
    pen = Turtle()

    angle = 360/sides

    for i in range(sides):
        pen.forward(sides_length)
        pen.right(angle)

    done()


def polygon_2(sides, sides_length):
    ''' Creates a polygon of sides n with each side of length sides_length using while loops'''

    # initializing the screen and the pen with minimal settings
    my_screen = Screen()
    my_screen.title('my Drawing')
    pen = Turtle()

    angle = 360/sides

    count = 0
    while count < sides:
        pen.forward(sides_length)
        pen.right(angle)
        count += 1  # what would happen if we move this line 'count+=1' at the beginning of the while loop?

    done()


def test_polygon():
    polygon(4, 100)  # change arguments for different shapes and sizes


def test_polygon_2():
    polygon_2(10, 30)  # change arguments for different shapes and sizes


test_polygon_2()
