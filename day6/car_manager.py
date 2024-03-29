from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def generate_car(self):
        random_car = Turtle(shape="square")
        random_car.penup()
        random_car.shapesize(stretch_wid=3)
        random_car.color(random.choice(COLORS))
        random_car.goto(280, random.randrange(-250, 250, 20))
        self.cars.append(random_car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
