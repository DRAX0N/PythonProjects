import colorgram
from turtle import Turtle, Screen, colormode
import random
# colors = colorgram.extract("spot_paint_2.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

# 10x10 circle
# 20 radius, 50 space

art = Turtle()
colormode(255)
number_of_circles = 100
row = range(10)
column = range(10)
art.speed("fastest")
art.penup()
art.setposition(-300, -300)
art.hideturtle()
for line in column:
    x = art.xcor()
    y = art.ycor()
    for place in row:
        # art.color(random.choice(color_list))
        # art.pendown()
        # art.begin_fill()
        # art.circle(20)
        # art.end_fill()
        art.dot(20, random.choice(color_list))
        # art.penup()
        art.forward(50)
    art.setposition(x, y+50)

screen = Screen()
screen.exitonclick()