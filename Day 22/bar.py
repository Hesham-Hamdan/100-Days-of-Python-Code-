from turtle import Turtle


class Bar(Turtle):
    def __init__(self, position_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 5)
        self.goto(position_x, 0)
        self.speed("fastest")
        self.setheading(90)

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)

    def bounce(self):
        if 300 - self.ycor() < 30:
            self.down()
        elif 300 - self.ycor() > 540:
            self.up()
