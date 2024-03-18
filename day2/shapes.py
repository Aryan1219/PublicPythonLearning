from turtle import Turtle
import random


def draw_shape(sides: int, turtle):
    angle = 360 / sides
    for i in range(sides):
        turtle.forward(100)
        turtle.right(angle)


t = Turtle()
draw_shape(3, t)
draw_shape(4, t)
draw_shape(5, t)
draw_shape(6, t)
draw_shape(7, t)
draw_shape(8, t)
draw_shape(9, t)
draw_shape(10, t)
