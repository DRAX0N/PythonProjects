from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []

turtles = []
x = -230
y = -100
for number in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[number])
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your answer was correct, winner {winning_color} turtle")
            else:
                print(f"Your turtle lost, winner {winning_color} turtle")

            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

    #
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def set_head_right():
#     tim.right(10)
#
# def set_head_left():
#     tim.left(10)
#
# def clean_screen():
#     tim.clear()
#     tim.home()
#     #tim.reset()
#
#
# screen.listen()
# screen.onkeypress(key="w", fun=move_forwards)
# screen.onkeypress(key="w", fun=move_forwards)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=set_head_left)
# screen.onkeypress(key="d", fun=set_head_right)
# screen.onkey(key="c", fun=clean_screen)
#
# # screen.onkey(key="W", fun=move_forwards)
# # screen.onkey(key="S", fun=move_backwards)
# # screen.onkey(key="A", fun=set_head_left)
# # screen.onkey(key="D", fun=set_head_right)
# # screen.onkey(key="C", fun=clean_screen)

screen.exitonclick()
