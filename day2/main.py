from turtle import Turtle, Screen
from random import choice

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
myturtle = Turtle()
myturtle.shape("circle")
myturtle.penup()
myturtle.goto(-200, 200)


for _ in range(1, 51):

    myturtle.pendown()
    myturtle.color(choice(colorlist))
    myturtle.stamp()
    myturtle.penup()
    myturtle.forward(30)
    if _ % 10 == 0:
        print(f"{myturtle.xcor()=},{myturtle.ycor()=}")
        myturtle.goto(-200, myturtle.ycor() - 60)

myturtle.hideturtle()
screen = Screen()
screen.exitonclick()
