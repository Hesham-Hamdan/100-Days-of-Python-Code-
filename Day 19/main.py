from turtle import Turtle, Screen
import turtle

screen = Screen()
t = Turtle()

# challenge 1


def mvforward():
    t.forward(10)


def mvbackward():
    t.backward(10)


def clearscreen():
    turtle.resetscreen()


def clockwise():
    t.right(10)


def counter_clockwise():
    t.left(10)


screen.listen()

screen.onkey(key="w", fun=mvforward)
screen.onkey(key="s", fun=mvbackward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clearscreen)

screen.exitonclick()
