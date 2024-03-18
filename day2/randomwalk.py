from turtle import colormode, Turtle, Screen
import random

directions = ["left", "right", "up", "down"]

colorlist = [
    "black",
    "blue",
    "brown",
    "chocolate",
    "cyan",
    "darkgreen",
    "gold",
    "gray",
    "green",
    "lightgreen",
    "magenta",
    "maroon",
    "navy",
    "orange",
    "purple",
    "red",
    "skyblue",
    "turquoise",
    "violet",
    "yellow",
]


def go(turtle, direction):

    if direction == "right":
        turtle.setheading(0)
    elif direction == "left":
        turtle.setheading(180)
    elif direction == "up":
        turtle.setheading(90)
    else:
        turtle.setheading(270)

    turtle.forward(50)


def linecolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


screen = Screen()
colormode(255)
t = Turtle()
t.pensize(15)
t.speed("fastest")
for i in range(1000):
    t.color(linecolor())
    direction = random.choice(directions)
    go(t, direction)

screen.exitonclick()
