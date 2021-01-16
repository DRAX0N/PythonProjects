import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.up, "Up")

score = Scoreboard()

car = []
for _ in range(20):
    obstacle = CarManager()
    car.append(obstacle)

czas = time.time()

game_is_on = True
while game_is_on:
    for _ in range(len(car)):
        car[_].car_move()
        if car[_].xcor() < -300:
            car[_].new_car_position()

    # if (car[len(car)-1].time + 0.8) < time.time():
    #     obstacle = CarManager(next)
    #     car.append(obstacle)

    player.reset_position()
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 280:
        for _ in range(len(car)):
            car[_].car_increase_speed()

    #detect collison with car
    for _ in range(len(car)):
        if player.distance(car[_]) < 35 and player.ycor() > car[_].ycor()-23 and player.ycor() < car[_].ycor()+23:
            score.game_over()
            game_is_on = False
    if player.ycor() > 280:
        score.score_level_up()

screen.exitonclick()


