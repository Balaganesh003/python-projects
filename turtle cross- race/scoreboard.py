from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.level = 1
        self.write(F"LEVEL{self.level}", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(F"LEVEL{self.level}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!", font=("Courier", 24, "normal"), align="center")
