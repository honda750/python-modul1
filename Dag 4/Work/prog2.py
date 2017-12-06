import turtle

def setupTurtle():
    myTurtleInside =  turtle.Turtle()
    myTurtleInside.penup()
    myTurtleInside.setpos(-300, 0)
    myTurtleInside.pendown()
    myTurtleInside.color('red')
    myTurtleInside.pensize(2.5)

    return myTurtleInside

averageTemperaturList = [3, 4, 6, 9, 14, 17, 18, 17, 14, 11, 7, 4]

def pulse(high, width):
    if high > 10:
        myTurtle.color('green')
    else:
        myTurtle.color('red')
    myTurtle.left((90))
    myTurtle.forward(high*10)
    myTurtle.right(90)
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(high*10)
    myTurtle.left(90)
    myTurtle.forward(width)

myTurtle = setupTurtle()
for temp in averageTemperaturList:
#for i in range(0, 3):
    pulse(temp, 25)

myTurtle.penup()
myTurtle.setpos(-250,250)
myTurtle.pendown()


turtle.done()