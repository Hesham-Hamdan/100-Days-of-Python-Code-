from turtle import Turtle


# HEADINGS = [0,90,180,]
# RANDOM_ANGLE = choice([30, 60, 120, 150, 210, 240, 300, 330])


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        # self.seth(RANDOM_ANGLE)
        self.x_move = 20
        self.y_move = 20
        self.move_speed = 0.1
