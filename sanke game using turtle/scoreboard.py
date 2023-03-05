from turtle import Turtle

ALIGNMENT = "center"
MOVE = False
FONT_SHAPE = "Arial"
FONT_SIZE = 20
FONT_TYPE = "normal"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.total_score = 0
        with open("data.txt") as file:
            score = file.read()
            self.high_score = int(score)
        self.write(arg=f"score:{self.total_score} HIGH SCORE{self.high_score}", move=MOVE, align=ALIGNMENT,
                   font=(FONT_SHAPE, FONT_SIZE, FONT_TYPE))

    def increase(self):
        self.total_score += 1
        self.write(arg=f"score:{self.total_score} HIGH SCORE{self.high_score}", move=MOVE, align=ALIGNMENT,
                   font=(FONT_SHAPE, FONT_SIZE, FONT_TYPE))

    def reset(self):
        if self.total_score > self.high_score:
            self.high_score=self.total_score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.total_score = 0
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"score:{self.total_score} HIGH SCORE{self.high_score}", move=MOVE, align=ALIGNMENT,
                   font=(FONT_SHAPE, FONT_SIZE, FONT_TYPE))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!", align=ALIGNMENT, font=(FONT_SHAPE, FONT_SIZE, FONT_TYPE))
