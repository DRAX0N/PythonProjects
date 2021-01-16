import turtle
import pandas

def write_state(name, x, y):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(x, y)
    text.write(f"{name}", False, align="center", font=("Arial", 10, "normal"))

screen = turtle.Screen()
screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

states = pandas.read_csv("50_states.csv")
list_states = states.state.to_list()
print(list_states)
# states[states.state == "Alaska"]
# print(states.x[states.state == "Alaska"])

score = 0
game_on = True
guessed_states = []


while game_on:
    answer_state = screen.textinput(title=f" {score}/50 +Guess the State", prompt="What's another state's name?")
    answer = answer_state.title()

    if answer in list_states:
        score += 1
        list_states.remove(answer)
        x = int(states.x[states.state == answer])
        y = int(states.y[states.state == answer])
        guessed_states.append(answer)
        write_state(answer, x, y)


    elif answer == "Exit":
        game_on = False
        pandas.DataFrame(list_states).to_csv("states_to_learn.csv")
#