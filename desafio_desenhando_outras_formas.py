from turtle import *

def drawSquare(size):
    for side in range(4):
        forward(size)
        left(90)

def drawTriangle(size):
    for side in range(3):
        forward(size)
        left(120)

bgcolor("MidnightBlue")
color("White")
pensize(3)

drawSquare(100)

penup()
forward(150)
pendown()

drawTriangle(100)

hideturtle()
done()
