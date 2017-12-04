"""
    Turtle: Draw two squares and a star inside.
"""
import turtle
import  math
myTurtle = turtle.Turtle()

myTurtle.penup()
myTurtle.setpos(-250,250)
myTurtle.pendown()

# Draw a square
i = 0
while i < 4:
    myTurtle. forward(500)
    myTurtle.right(90)
    i = i + 1

# Draw a square inside the first
myTurtle.penup()
myTurtle.setpos(-230,230)
myTurtle.pendown()
i = 0
while i < 4:
    myTurtle. forward(460)
    myTurtle.right(90)
    i = i + 1

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
