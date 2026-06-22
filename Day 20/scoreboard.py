from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score(1)

    def update_score(self, score):
        self.clear()
        self.write(f"Score: {score}", align=ALIGNMENT, font=FONT)
