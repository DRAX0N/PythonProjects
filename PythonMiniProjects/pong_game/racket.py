from turtle import Turtle

N = 90
S = 270
E = 0
W = 180

class Racket(Turtle):

    def __init__(self, player):
        super().__init__()
        self.create_racket(player)

    def create_racket(self, position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5, outline=1)
        self.setheading(N)
        self.penup()
        if position == 1:
            self.setposition(-350, 0)
        elif position == 2:
            self.setposition(350, 0)

        # for number in range(racket_length):
        #     new_racket = Turtle(shape="square")
        #     new_racket.shapesize(0.75)
        #     new_racket.color("white")
        #     new_racket.penup()
        #     new_racket.speed("fastest")
        #     y -= 15
        #     new_racket.goto(x, y)
        #     self.racket.append(new_racket)

    # def move_racket(self, direction):
    #     self.forward(1)

        # if direction == 0:
        #     for racket_body in range(len(self.racket)-1, 0, -1):
        #         # new_x = self.racket[racket_body-1].xcor()
        #         # new_y = self.racket[racket_body - 1].ycor()
        #         # self.racket[racket_body].goto(new_x, new_y)
        #         new_position = self.racket[racket_body-1].position()
        #
        #         self.racket[racket_body].goto(new_position)
        #     self.head.forward(STEP)
        # elif direction == 1:
        #     for racket_body in range(0, len(self.racket)-1):
        #         # new_x = self.racket[racket_body-1].xcor()
        #         # new_y = self.racket[racket_body - 1].ycor()
        #         # self.racket[racket_body].goto(new_x, new_y)
        #         new_position = self.racket[racket_body+1].position()
        #
        #         self.racket[racket_body].goto(new_position)
        #     self.racket[3].forward(STEP)

    def up(self):
        if self.ycor() < 250:
            self.forward(10)
        # up = 0
        # # self.head.setheading(N)
        # self.move_racket(up)

    def down(self):
        if self.ycor() > -250:
            self.backward(10)
        # down = 1
        # # self.racket[3].setheading(S)
        # self.move_racket(down)