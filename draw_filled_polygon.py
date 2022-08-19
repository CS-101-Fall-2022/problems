# Author: S. Muhammad Ali
# Date: Fall 2022 semester
# Course: CS 101 Programming Fundamentals
# Purpose: Drawing filled polygons using python's turtle library
# Reference: https://docs.python.org/3/library/turtle.html
# Functions:
#   - polygon: draws polygon using for loop.
#   - polygon_2: draws polygon using while loop.
#   - main: prompt user for input, does error checking and then calls either of the above functions.
# Concepts: the implementation below uses
#   - Usage of 'turtle', a built in library
#   - functions
#   - modular arithmetic
#   - iteration
#   - variables
#   - User input
#   - String method isdigit()
# Variations:
#   - The code demonstrates how for loop can be used in place of while loops.
#   - Try, except can be used for error checking


from turtle import *  # imports all functions from the Turtle library/module


def polygon(sides, sides_length):
    ''' Creates a filled polygon of sides n with each side of length sides_length using for loops'''

    # initializing the screen and the pen with minimal settings
    my_screen = Screen()
    my_screen.title('my Drawing')
    pen = Turtle()

    angle = 360/sides
    pen.begin_fill()
    pen.color('red')  # Change fill color as you like
    for i in range(sides):
        pen.forward(sides_length)
        pen.right(angle)
    pen.end_fill()

    done()


def polygon_2(sides, sides_length):
    ''' Creates a polygon of sides n with each side of length sides_length using while loops'''

    # initializing the screen and the pen with minimal settings
    my_screen = Screen()
    my_screen.title('my Drawing')
    pen = Turtle()

    angle = 360/sides

    count = 0  # initializes counter to zero.

    pen.begin_fill()
    pen.color('blue')  # Change fill color as you like
    while count < sides:
        pen.forward(sides_length)
        pen.right(angle)
        count += 1  # Increases value of count by 1 in each iteration. What would happen if we move this line 'count+=1' at the beginning of the while loop?
    pen.end_fill()

    done()


def main():

    n = input('Please enter the no of sides')
    length = input('Please enter the length of each side')
    if n.isdigit() == False or length.isdigit() == False: # checks if the input is correct, and calls the function again incase the input is invalid.
        print('Your input is invalid. Please enter integers for the input fields.')
        main()

    else:
        polygon(int(n), float(length))
        # polygon_2(n, length)
