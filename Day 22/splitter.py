from turtle import Turtle


class Splitter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, -280)
        self.seth(90)
        self.pencolor("white")
        self.draw()

    def draw(self):
        for num in range(0, 100):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
