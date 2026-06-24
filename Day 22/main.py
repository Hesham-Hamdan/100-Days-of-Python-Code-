import time
from turtle import Screen
from bar import Bar
from splitter import Splitter


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

splitter = Splitter()
left_bar = Bar(-370)
right_bar = Bar(370)


game_is_on = True

screen.listen()


while game_is_on:
    time.sleep(0.1)
    screen.update()
    left_bar.forward(20)
    right_bar.forward(20)


screen.exitonclick()
