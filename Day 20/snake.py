from turtle import Turtle

STARTING_X = [0, -20, -40]
MOVING_DISTANCE = 20

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for x in STARTING_X:
            self.add_segment((x, 0))

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.setposition(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num - 1].xcor()
            new_y = self.segments[num - 1].ycor()
            self.segments[num].goto(new_x, new_y)

        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
