import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

score = 1

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1
        scoreboard.update_score(score)
        snake.extend()

    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
