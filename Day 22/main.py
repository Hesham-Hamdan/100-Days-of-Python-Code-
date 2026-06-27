import time
from turtle import Screen
from bar import Bar
from splitter import Splitter

from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

splitter = Splitter()
left_bar = Bar(-370)
right_bar = Bar(370)
ball = Ball()


game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=right_bar.up)
screen.onkey(key="Down", fun=right_bar.down)
screen.onkey(key="w", fun=left_bar.up)
screen.onkey(key="s", fun=left_bar.down)

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    left_bar.forward(20)
    right_bar.forward(20)
    right_bar.bounce()
    left_bar.bounce()
    ball.move()
    ball.wall_bounce()


screen.exitonclick()
