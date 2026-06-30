from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-280, 240)
        self.hideturtle()
        self.update_score(1)

    def update_score(self, score):
        self.clear()
        self.write(f"Level: {score}", align="left", font=FONT)
