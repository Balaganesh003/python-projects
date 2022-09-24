import turtle
from turtle import Turtle, Screen
import colorgram
import random

turtle.colormode(255)
total_colors = [
    (233, 232, 231), (232, 233, 237), (236, 231, 234), (230, 234, 231), (200, 162, 91), (168, 66, 50), (159, 58, 72),
    (127, 163, 189), (224, 206, 117), (214, 84, 54), (63, 35, 53), (202, 136, 160), (41, 37, 65), (57, 49, 104),
    (66, 83, 147), (196, 81, 119), (128, 179, 158), (158, 168, 69), (74, 127, 96), (80, 154, 114), (113, 43, 37),
    (72, 48, 38), (120, 40, 47), (160, 200, 217), (98, 107, 166), (219, 176, 186), (224, 175, 169), (183, 185, 210),
    (175, 203, 185), (89, 147, 160), (82, 61, 42)]

# here colorgram is used to get the colors in the image in the form of RGB number and stored has tuples
# the below code is used to convert the RGB output into tuples and append each color into a same list
# colors_palatte = colorgram.extract("image.jpg", 100)
# for colour in range(len(colors_palatte)):
#     first_color = colors_palatte[colour]
#     single_color = []
#     rgb = first_color.rgb
#     single_color.append(rgb[0])
#     single_color.append(rgb[1])
#     single_color.append(rgb[2])
#     total_colors.append(tuple(single_color))

timmy = Turtle()
timmy.pensize(15)
timmy.penup()
timmy.hideturtle()
timmy.setx(-200)
timmy.sety(-200)
timmy.speed(100)
x_coordinate = timmy.xcor()
y_coordinate = timmy.ycor()


def draw_line():
    for i in range(10):
        current_color = random.choice(total_colors)
        timmy.pendown()
        timmy.dot(15, current_color)
        timmy.penup()
        timmy.forward(50)


for _ in range(10):
    timmy.setx(x_coordinate)
    timmy.sety(y_coordinate)
    draw_line()
    y_coordinate += 50
    timmy.penup()
# print(total_colors)

screen = Screen()
screen.exitonclick()
