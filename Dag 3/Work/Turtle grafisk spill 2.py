"""
    Grafisk spill 2 med turle. Flere mål.
    (Husk at vindu må være aktivt for at pilene fungerer)
"""
import turtle
import math
import random

# Skjerm
skjerm = turtle.Screen()
skjerm.bgcolor('lightgreen')
skjerm.tracer(3)            # Gjør skjeroppdatering raskere
# Tegn ramme
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
maxMål = 6      # Antall mål
mål = []        # Definerer tom liste

for nummer in range(maxMål):                # range = 0 til (maxMål - 1)
    mål.append(turtle.Turtle())             # legger ett objekt (mål) i hver posisjon i listen
    mål[nummer].color('red')                # setter farge på hvert objekt.
    mål[nummer].shape('circle')             # setter utforming (shape) på hvert objekt
    mål[nummer].penup()
    mål[nummer].speed(0)
    mål[nummer].setposition(random.randint(-280,280), random.randint(-280,280)) # random plassering

# Sett hastighet
hastighet = 1

# Definer funksjoner
def snuVenstre():       # Venstre piltast
    spiller.left(30)

def snuHøyre():         # Høyre piltast
    spiller.right(30)

def økHastighet():      # Opp piltast
    global hastighet
    hastighet += 1

def erDetKollisjon(t1,t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
    if (d < 20):        # d = avstand mellom spiller og mål
        return True
    else:
        return False


# Sett tangentbort bindinger.  Disse blir fast definert og trenger ikke ligge i program loop.
turtle.listen()
turtle.onkey(snuVenstre,"Left") # Pil venstre snur spiller
turtle.onkey(snuHøyre,'Right')  # Pil høyre snur spiller
turtle.onkey(økHastighet,'Up')  # Pil opp øker hastihet på spiller

while True:
    spiller.forward(hastighet) # Flytter spiller
    # Snur spiller hvis den treffer rammen
    if (spiller.xcor() > 280 or spiller.xcor() < -280):
        spiller.right(180)
    if (spiller.ycor() > 280 or spiller.ycor() < -280):
        spiller.right(180)

    # Snur målene hvis de treffer rammen
    for nummer in range(maxMål):
        mål[nummer].forward(1)  # Flytter målene
        if (mål[nummer].xcor() > 270 or mål[nummer].xcor() < -270):
            mål[nummer].right(180)
        if (mål[nummer].ycor() > 270 or mål[nummer].ycor() < -270):
            mål[nummer].right(180)

        # Kollisjon sjekk. Gir ny posisjon og ny vinkel på mål ved kollisjon.
        if (erDetKollisjon(spiller, mål[nummer])):
            mål[nummer].setposition(random.randint(-280, 280), random.randint(-280, 280)) # Ny posisjon
            mål[nummer].right(random.randint(0, 360))  # Ny vinkel


delay = raw_input('Trykk ENTER for å avslutte.')

turtle.done()