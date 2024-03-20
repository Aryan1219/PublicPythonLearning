from turtle import Turtle, Screen


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
turtles = []
for i in range(3):
    turtles.append(Turtle(shape="square"))
    turtles[i].color("yellow")
    turtles[i].penup()

turtles[1].goto(-20, 0)
turtles[2].goto(-40, 0)


screen.exitonclick()