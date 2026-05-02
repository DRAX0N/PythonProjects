from turtle import Turtle
import time
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
W = 180

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2, outline=1)
        self.color_definition()
        self.setheading(W)
        self.penup()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_start_position()
        self.time = time.time()

    def color_definition(self):
        self.color(random.choice(COLORS))

    def car_move(self):
        self.forward(self.car_speed)

    def car_increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def car_start_position(self):
        y = random.randint(-240, 240)
        x = random.randint(-260, 260)
        self.goto(x, y)

    def new_car_position(self):
        x = random.randint(300, 460)
        y = random.randint(-240, 240)
        self.goto(x, y)
