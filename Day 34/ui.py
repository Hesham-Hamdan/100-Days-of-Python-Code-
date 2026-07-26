from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.scoreboard = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.scoreboard.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Amazon accquired Twitch in August",
            font=("Ariel", 15, "italic"),
            fill=THEME_COLOR,
        )

        self.window.mainloop()
