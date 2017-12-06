"""
    Turtle:  Draw two squares and a star inside.
"""
import turtle
import  math

myTurtle = turtle.Turtle()

# Draw a square
def drawSquare(startX, startY, side):
    myTurtle.penup()
    myTurtle.setpos(startX, startY,)
    myTurtle.pendown()
    i = 0
    while i < 4:
        myTurtle.forward(side)
        myTurtle.right(90)
        i = i + 1

drawSquare(-250,250,500)
drawSquare(-230,230,460)

# Draw a star inside the squares
myTurtle.penup()
myTurtle.setpos(0,150)
myTurtle.pendown()
i = 0
myTurtle.right(252)
while i < 5:
    myTurtle. forward(300/(math.cos(72)))
    myTurtle.right(144)
    i = i + 1

turtle.done()
