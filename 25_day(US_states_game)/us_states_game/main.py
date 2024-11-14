import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
csv_file = "50_states.csv"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states = data.state.to_list()

def draw_text(data):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x=int(data.x), y=int(data.y))
    t.write(data.state.item())

guessed_list = []
while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 Guess the State", prompt="What's another state's name?").title()

    element = data[data.state == answer_state]

    if answer_state == "Exit":
        to_learn = [i for i in states if i not in guessed_list]
        new_csv = pandas.DataFrame(to_learn).to_csv("states_to_learn.csv")
        break

    if not element.empty and answer_state not in guessed_list:
        draw_text(element)
        guessed_list.append(answer_state)



