from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, x_postion):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x_postion, 260)
        self.hideturtle()
        self.update_score(0)

    def update_score(self, score):
        self.clear()
        self.write(f"{score}", align=ALIGNMENT, font=FONT)
