"""
Function Name: turtleTime
Parameters: shape (int)
Returns: image of the shape with n number of lines
"""

import turtle

#SOLUTION CODE
def turtleTime (shape) :
    rotate = 360 / shape
    t = turtle.Pen()
    if shape == 1:
        t.circle(100)
    else :
        for i in range(shape) :
            t.forward(100)
            t.left(rotate)

#TEST CASE(S)
turtleTime(3)
#Triangle
turtleTime(1)
#Circle
turtleTime(7)
#Heptagon
