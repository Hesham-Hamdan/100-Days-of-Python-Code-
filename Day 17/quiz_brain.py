class QuizBrain:
    def __init__(self, list):
        self.question_num = 0
        self.question_list = list
        self.user_score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right")
            self.user_score += 1
        else:
            print("wrong answer")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.user_score} / {self.question_num}")
