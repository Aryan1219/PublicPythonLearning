import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Objects Created
player = Player()
screen.onkey(player.move,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

