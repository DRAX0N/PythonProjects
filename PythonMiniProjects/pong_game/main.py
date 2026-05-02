from turtle import Screen, Turtle
from racket import Racket
from ball import Ball
from scoreboard import Scoreboard
import time

#MAIN
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#
# rectCors = ((-20,10),(20,10),(20,-10),(-20,-10));
# screen.register_shape('rectangle',rectCors);

# Middle line
line = Turtle()
line.color("white")
line.hideturtle()
line.penup()
line.goto(0, 300)
line.setheading(270)
line.pensize(5)
for _ in range(15):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

# Racket
s = Turtle()
# s.shape("rectangle")
# s.color("white")

player_one = 1
player_two = 2

player1 = Racket(player_one)
player2 = Racket(player_two)
screen.listen()
screen.onkeypress(player1.up, "w")
screen.onkeypress(player1.down, "s")
screen.onkeypress(player2.up, "Up")
screen.onkeypress(player2.down, "Down")
score = Scoreboard()
ball = Ball()

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    # Detect wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect racket on the right
    if ball.xcor() > 320 and ball.distance(player2) < 50 or ball.xcor() < -320 and ball.distance(player1) < 50:
        ball.bounce_x()

    # Detect miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_score += 1
        score.score_update()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_score += 1
        score.score_update()
    ball.ball_move()

screen.exitonclick()
