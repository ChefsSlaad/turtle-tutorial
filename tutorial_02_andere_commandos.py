# we beginnen met een nieuw grogramma, dus we moeten weer
from turtle import *

# naast forward() en right() zijn er nog een paar andere handige commando's

left(90)            # doet wat je verwacht had. right(270) is hetzelfde and left(90)

backward(100)       # doet ook al wat je verwacht had.
forward(50)         # zet een lijn de helft van de lengte van forward(100). 
                    # 2x raden wat forward(200) doet


color("red")        # veranderd de kleur van de pen naar rood. je ziet het effect 
                    # pas nadat je wat getekend hebt met forward(100) of backward(100) 
                    # probeer ook eens wat andere kleuren zoals "green", "yellow", 
                    # "blue", "pink", "black" of "white". let op de aanhalingstekens

bgcolor("black")    # stelt de kleur van de achtergrond in. probeer eens een paar 
                    # kleuren 

circle(100)         # tekent een cirkel met een straal van 100. probeer eens cirkels
                    # met andere stralen

penup()             # til de pen op. Forward(100) beweegt de pen nog steeds vooruit 
                    # maar je tekent geen lijn
pendown()           # zet de pen weer neer

pensize(2)          # stel de dikte van de pen in op 2 pixels. probeer eens 
                    # verschillende diktes

home()              # ga terug naar het beginpunt

clear()             # maak het scherm weer leeg


