from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
N = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(N)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
