import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
img = "C:/Users/DELL/OneDrive/Desktop/coding/python/Day 25/US-state-game/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


t = turtle.Turtle()
t.penup()
t.hideturtle()


def get_question():
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    return answer_state


data = pd.read_csv("C:/Users/DELL/OneDrive/Desktop/coding/python/Day 25/US-state-game/50_states.csv")
states = data.state.to_list()


class State:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.show_name()

    def show_name(self):
        t.goto(self.x, self.y)
        t.write(self.name, align="center", font=("Arial", 8, "normal"))


guessed_states = []
while True:
    answer_state = get_question()
    if answer_state == "Exit":
        break
    if answer_state in states and answer_state not in guessed_states:
        state_data = data[data.state == answer_state]
        state = State(int(state_data.x), int(state_data.y), answer_state)
        guessed_states.append(answer_state)
    else:
        print("Incorrect or already guessed")

turtle.mainloop()
