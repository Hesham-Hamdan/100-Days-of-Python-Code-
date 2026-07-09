import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25\states game\states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("Day 25/states game/50_states.csv")


title = "Guess the state"
game_is_on = True
guessed_states = []

while game_is_on:
    answer_state = screen.textinput(
        title=title, prompt="What's another state's name? "
    ).title()

# for state in data["state"].to_list():
#     if state not in guessed_states:
#         not_guessed["state"].append(state)
