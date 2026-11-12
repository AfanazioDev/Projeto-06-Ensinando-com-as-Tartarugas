from turtle import *

# Desenha um planeta usando tamanho e cor
def drawPlanet(planetSize, planetColour):
    color(planetColour)
    pendown()
    begin_fill()
    circle(planetSize)
    end_fill()
    penup()

bgcolor("MidnightBlue")

drawPlanet(30, "Blue")

penup()
goto(100, 0)
pendown()
drawPlanet(20, "Red")

penup()
goto(-100, -100)
pendown()
drawPlanet(40, "Green")

hideturtle()
done()
