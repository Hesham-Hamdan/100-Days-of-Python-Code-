import time
from turtle import Screen
from bar import Bar
from splitter import Splitter
from scoreboard import Scoreboard
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
left_scoreboard = Scoreboard(-100)
right_scoreboard = Scoreboard(100)
left_score = 0
right_score = 0


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
    ball.bar_bounce(left_bar)
    ball.bar_bounce(right_bar)
    if ball.xcor() > 390:
        ball.reset()
        left_score += 1
        left_scoreboard.update_score(left_score)
    if ball.xcor() < -390:
        ball.reset()
        right_score += 1
        right_scoreboard.update_score(right_score)


screen.exitonclick()
