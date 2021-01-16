from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.high_score_read()
        self.color("white")
        self.goto(0, 275)
        self.score_print()

    def high_score_read(self):
        with open("data.txt") as file:
            self.high_score = file.read()

    def score_update(self):
        self.score += 1
        self.score_print()

    def score_print(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", False, align="center", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.score_print()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over", False, align="center", font=("Arial", 24, "normal"))