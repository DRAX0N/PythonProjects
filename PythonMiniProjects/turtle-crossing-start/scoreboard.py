from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(-210, 245)
        self.score_print()


    def score_print(self):
        self.clear()
        self.write(f"Level: {self.score}", False, align="center", font=FONT)

    def score_level_up(self):
        self.score += 1
        self.score_print()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=FONT)