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

        true_image = PhotoImage(file="Day 34/images/true.png")
        false_image = PhotoImage(file="Day 34/images/false.png")

        self.right_button = Button(image=true_image, highlightthickness=0)
        self.right_button.grid(row=2, column=0, pady=20)
        self.wrong_button = Button(image=false_image, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1, pady=20)

        self.next_question()

        self.window.mainloop()
