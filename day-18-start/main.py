from turtle import Turtle, Screen, colormode
import random


def random_turtle_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def choose_direction():
    angle = random.choice([0, 90, 180, 270])
    return angle


tim = Turtle()
tim.shape("arrow")
colormode(255)
#tim.pensize(10)
tim.speed("fastest")
steps = 200

for _ in range(0, 360,10):
    tim.color(random_turtle_color())
    tim.setheading(_)
    tim.circle(100)

# for _ in range(steps):
#     tim.color(random_turtle_color())
#     tim.forward(20)
#     tim.setheading(choose_direction())

# for n in range(4):
#     tim.forward(100)
#     tim.left(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#r = random.choice(range(255))


# for shape in range(3, 10):
#     tim.color(random_turtle_color())
#     angle = 360 / shape
#     for _ in range(shape):
#         tim.forward(100)
#         tim.right(angle)

screen = Screen()
screen.exitonclick()