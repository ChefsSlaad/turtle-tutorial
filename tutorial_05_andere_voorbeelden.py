# bekijk hieronder een paar andere programma's

from turtle import *

while True:
    forward(200)
    left(170)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(121):
    pencolor(colors[i%6])
    circle(30 +i)
    right(3)



# spider web

def web(size, webs):
    sides = 6
    angle = 360 / sides
    distance = size //(webs+1) 
    #teken eerst de middenlijnen
    for i in range(sides):
        forward(size)
        backward(size)
        right(angle)

    # teken nu de draden van het webs

    for w in range(webs):
        forward(distance)
        right(angle)
        for s in range(sides):
            right(angle)
            forward(distance*(w+1))
        # terug naar de middenlijnen
        left(angle)
web(250,6)
