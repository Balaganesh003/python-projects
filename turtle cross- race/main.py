import time
import turtle
from turtle import Screen
from player import Player

from car_manager import CarManager
from scoreboard import Scoreboard
TIMESLEEP=.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    car_manager.create_cars()
    car_manager.move_left()
    time.sleep(TIMESLEEP)
    screen.update()

    #     detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #             detect player has reached the top
    if player.reach_top():
        scoreboard.level_up()
        TIMESLEEP*=.6


screen.exitonclick()
