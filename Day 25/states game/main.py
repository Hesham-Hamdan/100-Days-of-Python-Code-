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
    if answer_state == "Exit":
        break
    state = data[data["state"] == answer_state]
    if len(state) >= 1:
        x_cor = max(state["x"])
        y_cor = max(state["y"])
        cors = (x_cor, y_cor)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.setpos(cors)
        t.write(f"{answer_state}", align="left", font=("Arial", 8, "normal"))
        guessed_states.append(answer_state)
        title = f"{len(guessed_states)}/50 States Correct"

not_guessed = {
    "state": [state for state in data["state"].to_list() if state not in guessed_states]
}
# for state in data["state"].to_list():
#     if state not in guessed_states:
#         not_guessed["state"].append(state)


data2 = pandas.DataFrame(not_guessed)
data2.to_csv("Day 25\states game\states_to_learn.csv")
