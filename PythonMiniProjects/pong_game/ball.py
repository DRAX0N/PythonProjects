from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.01

    def ball_move(self):
        # end_y = random.randint(-300, 300)

        start_x = self.xcor()
        start_y = self.ycor()
        new_x = start_x + self.x_move
        # if self.ycor() >= 280:
        # if direction == 1:
        #     self.y_move *= -1
        # if self.ycor() < 280 and self.ycor() > -280:
        new_y = start_y + self.y_move

        self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.bounce_x()

    # def ball_speed(self):
    #     self.x_move += 1
    #     self.y_move += 1
