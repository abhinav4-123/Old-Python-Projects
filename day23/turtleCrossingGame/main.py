import time
from turtle import Screen
from player import Player,FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20 :
            game_is_on = False
            scoreboard.game_over()
    # if player.ycor() > FINISH_LINE_Y:
    #     time.sleep(0.2)
    #     player.start()
    #     car_manager.change_level()
    #     scoreboard.update_scoreboard()

    # detect successful collision
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.next_level()
        scoreboard.increase_level()


screen.exitonclick()