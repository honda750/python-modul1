"""
    Grafisk spill 1 med turle. Ett mål. (Husk at vindu må være aktivt for at pilene fungerer)
"""
import turtle
import math
import random

# Skjerm
skjerm = turtle.Screen()
skjerm.bgcolor('lightgreen')

#  Tegn ramme
minPenn = turtle.Turtle()
minPenn.penup()
minPenn.setposition(-280, -280)
minPenn.pendown()
minPenn.pensize(3)

for side in range(4):   # Tegner ramme
    minPenn.forward(560)
    minPenn.left(90)
minPenn.hideturtle()


# Lag spiller
spiller = turtle.Turtle()
spiller.color('blue')
spiller.shape('triangle')
spiller.penup()

# Mål
mål = turtle.Turtle()
mål.color('red')
mål.shape('circle')
mål.penup()
mål.speed(0)
#mål.setposition(-100,-100)
mål.setposition(random.randint(-280,280), random.randint(-280,280))
# Sett hastighet
hastighet = 1

# Definer funksjoner
def snuVenstre():
    spiller.left(30)

def snuHøyre():
    spiller.right(30)

def økHastighet():
    global hastighet
    hastighet += 1

def erDetKollisjon(t1,t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if (d < 20):
        return True
    else:
        return False


# Sett tangentbort bindinger
turtle.listen()
turtle.onkey(snuVenstre,"Left")
turtle.onkey(snuHøyre,'Right')
turtle.onkey(økHastighet,'Up')

while True:
    spiller.forward(hastighet)
    # Posisjon sjekk
    if (spiller.xcor() > 280 or spiller.xcor() < -280):
        spiller.right(180)
    if (spiller.ycor() > 280 or spiller.ycor() < -280):
        spiller.right(180)

    # Kollisjon sjekk
    if (erDetKollisjon(spiller, mål)):
        mål.setposition(random.randint(-280,280), random.randint(-280,280))
        mål.right(random.randint(0, 360))

    # Flytt målet
    mål.forward(1)
    if (mål.xcor() > 270 or mål.xcor() < -270):
        mål.right(180)
    if (mål.ycor() > 270 or mål.ycor() < -270):
        mål.right(180)

delay = raw_input('Trykk ENTER for å avslutte.')


turtle.done()