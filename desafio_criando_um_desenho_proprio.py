from turtle import *

# Função para desenhar um quadrado
def drawSquare(size, colorName):
    color(colorName)
    begin_fill()
    for side in range(4):
        forward(size)
        left(90)
    end_fill()

# Função para desenhar um triângulo
def drawTriangle(size, colorName):
    color(colorName)
    begin_fill()
    for side in range(3):
        forward(size)
        left(120)
    end_fill()

# Função para desenhar um retângulo
def drawRectangle(width, height, colorName):
    color(colorName)
    begin_fill()
    for side in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

# Configuração da tela
bgcolor("LightSkyBlue")
speed(5)
pensize(2)

# Desenha o sol
penup()
goto(250, 180)
pendown()
color("Yellow")
begin_fill()
circle(40)
end_fill()

# Desenha o corpo da casa
penup()
goto(-100, -100)
setheading(0)
pendown()
drawSquare(200, "Wheat")

# Desenha o telhado
penup()
goto(-100, 100)
setheading(0)
pendown()
drawTriangle(200, "Red")

# Desenha a porta
penup()
goto(-25, -100)
setheading(0)
pendown()
drawRectangle(50, 90, "SaddleBrown")

# Desenha a janela esquerda
penup()
goto(-80, 0)
setheading(0)
pendown()
drawSquare(45, "DeepSkyBlue")

# Desenha a janela direita
penup()
goto(35, 0)
setheading(0)
pendown()
drawSquare(45, "DeepSkyBlue")

# Finalização
hideturtle()
done()
