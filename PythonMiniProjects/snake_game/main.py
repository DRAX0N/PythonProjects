from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# snake = Turtle()
# snake.shape("square")
# snake.color("white")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Food detect
    if snake.head.distance(food) < 15:
        snake.extend_snake()
        food.refresh()
        score.score_update()

    # Wall detect
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # score.game_over()
        # game_on = False
        score.reset()
        snake.reset()
    # Tail detect
    for element in snake.snake[1:]:
        if snake.head.distance(element) < 10:
            # score.game_over()
            # game_on = False
            score.reset()
            snake.reset()

screen.exitonclick()