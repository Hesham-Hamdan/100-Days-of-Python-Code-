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
