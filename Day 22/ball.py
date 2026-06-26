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

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        if self.ycor() > 280 or self.ycor() < -280:
            # new_heading = 360 - self.heading()
            # self.setheading(new_heading)
            self.y_move *= -1

    def bar_bounce(self, bar):
        if self.distance(bar) < 80 and (self.xcor() > 320 or self.xcor() < -320):
            # new_heading = 90 + self.heading()
            # self.setheading(new_heading)
            self.x_move *= -1
            self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.wall_bounce()
        self.move_speed = 0.1
