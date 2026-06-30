from random import choice, randint
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(choice(COLORS))
        self.shapesize(0.5, 1)
        self.seth(180)
        self.starting_cars_positions()
        self.starting_speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.starting_speed)

    def starting_cars_positions(self):
        random_x = randint(-300, 400)
        random_y = randint(-250, 250)
        self.goto(random_x, random_y)

    def increase_speed(self):
        self.starting_speed += MOVE_INCREMENT
