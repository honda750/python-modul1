"""
    Grafisk spill 2 med turle. Flere mål. (Husk at vindu må være aktivt for at pilene fungerer)
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

# Lag Mål

maxMål = 4      # Antall mål
mål[]           # Definerer tom liste

for nummer in range(maxMål):
    mål[nummer].append(turtle.Turtle())
    mål[nummer].color('red')
    mål[nummer].shape('circle')
    mål[nummer].penup()
    mål[nummer].speed(0)
    mål[nummer].setposition(random.randint(-280,280), random.randint(-280,280))
#mål.setposition(-100,-100)

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
    for nummer in range maxMål
        mål[nummer].forward(1)
        if (mål[nummer].xcor() > 270 or mål[nummer].xcor() < -270):
            mål[nummer].right(180)
        if (mål[nummer].ycor() > 270 or mål[nummer].ycor() < -270):
            mål[nummer].right(180)

        # Kollisjon sjekk
        if (erDetKollisjon(spiller, mål)):
            mål[nummer].setposition(random.randint(-280, 280), random.randint(-280, 280))
            mål[nummer].right(random.randint(0, 360))




delay = raw_input('Trykk ENTER for å avslutte.')


turtle.done()