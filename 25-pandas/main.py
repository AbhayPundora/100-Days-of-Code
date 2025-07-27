import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_guesses = 0
NUMBER_OF_STATES = 50
guessed_states = []

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{correct_guesses}/50 States correct", prompt="What's another state's name?").title()
    # print(answer_state)

    states = pandas.read_csv("50_states.csv")
    # print(states)

    if answer_state == "Exit":
        break

    if correct_guesses == NUMBER_OF_STATES:
        game_is_on = False

    user_guess = states[states.state == answer_state]
    if not user_guess.empty:
            guessed_states.append(user_guess.state.item)
            new_state = turtle.Turtle()
            x = user_guess["x"].item()
            y = user_guess["y"].item()
            new_state.hideturtle()
            new_state.penup()
            new_state.goto(x,y)
            new_state.write(answer_state)
            correct_guesses += 1


all_states = states["state"].to_list()

not_guessed_states = [state for state in all_states if state not in guessed_states]

not_guessed_states_dict = {
    "states": not_guessed_states
}
data = pandas.DataFrame(not_guessed_states_dict)

data.to_csv("not_guessed_states.csv")













