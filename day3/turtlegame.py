from turtle import Turtle, Screen
import random

colorlist = [
    "black",
    "blue",
    "brown",
    "red",
    "yellow",
    "green",
]
screen = Screen()
screen.setup(width=800, height=800)
Turtles = []
for i in range(len(colorlist)):
    Turtles.append(Turtle(shape="turtle"))
    Turtles[i].color(colorlist[i])
    Turtles[i].penup()
j = -150
for i in range(len(Turtles)):
    Turtles[i].goto(-350, j)
    j += 50
choice = screen.textinput("Color", "Color to bet on: ")


race_is_going = True
while race_is_going:
    for t in Turtles:
        if t.xcor() > 380:
            if t.pencolor() == choice:
                print(f"You have won! The winning turtle was {t.pencolor()}!")
                race_is_going = False
                break

            else:
                print(f"You have lost! The winning turtle was {t.pencolor()}!")
                race_is_going = False
                break
        t.forward(random.randint(0, 20))


screen.exitonclick()
