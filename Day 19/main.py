import random
from turtle import Turtle, Screen
import turtle

screen = Screen()


# challenge 1

# def mvforward():
#     t.forward(10)


# def mvbackward():
#     t.backward(10)


# def clearscreen():
#     turtle.resetscreen()


# def clockwise():
#     t.right(10)


# def counter_clockwise():
#     t.left(10)


# screen.listen()

# screen.onkey(key="w", fun=mvforward)
# screen.onkey(key="s", fun=mvbackward)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="c", fun=clearscreen)

screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


# challenge 2

ys = [-125, -75, -25, 25, 75, 125]
names = ["timmy", "jimmy", "limmy", "simmy", "kimmy", "himmy"]

turtles = []
index = 0
for y in ys:
    turtles.append(Turtle(shape="turtle"))
    turtles[index].color(colors[index])
    turtles[index].penup()
    turtles[index].goto(-230, y)
    index += 1


race = False

if user_bet:
    race = True

while race:
    for tur in turtles:
        random_steps = random.randint(0, 10)
        if tur.xcor() > 230:
            race = False
            winning_turtle = tur.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner")
            else:
                print(f"You've lost! The {winning_turtle} is the winner")
        tur.forward(random_steps)

screen.listen()
screen.exitonclick()
