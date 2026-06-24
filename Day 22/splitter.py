from turtle import Turtle


class Splitter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, -280)
        self.seth(90)
        self.pencolor("white")
