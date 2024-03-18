from turtle import Turtle, Screen, colormode
from random import randint

turtle = Turtle()
colormode(255)
turtle.speed("fastest")

for i in range(360):
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    turtle.circle(100)
    turtle.right(1)
screen = Screen()
screen.exitonclick()
