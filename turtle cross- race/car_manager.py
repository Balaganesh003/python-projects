from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_cars(self):

        random_choice=random.randint(1,6)
        if random_choice==1 :
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.setheading(180)
            new_car.shapesize(stretch_len=3, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-300, 300))
            self.all_cars.append(new_car)


    def move_left(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    # def increasespeed(self):
    #     self.car_speed+=MOVE_INCREMENT


