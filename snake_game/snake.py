from turtle import Screen, Turtle

STEP = 20

N = 90
S = 270
E = 0
W = 180

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        x = 0
        y = 0
        snake_length = 3
        for number in range(snake_length):
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            x -= 20
            self.snake.append(new_snake)

    def extend_snake(self):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        x_head = self.snake[-1].xcor()
        y_head = self.snake[-1].ycor()
        new_snake.goto(x=x_head, y=y_head)
        self.snake.append(new_snake)

    def move(self):
        for snake_body in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[snake_body-1].xcor()
            new_y = self.snake[snake_body - 1].ycor()
            self.snake[snake_body].goto(new_x, new_y)
            # new_position = snake[snake_body-1].position()
            # snake[snake_body].goto(new_position)
        self.head.forward(STEP)

    def reset(self):
        for _ in self.snake:
            _.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def up(self):
        if self.head.heading() != S:
            self.head.setheading(N)

    def down(self):
        if self.head.heading() != N:
            self.head.setheading(S)

    def left(self):
        if self.head.heading() != E:
            self.head.setheading(W)

    def right(self):
        if self.head.heading() != W:
            self.head.setheading(E)
