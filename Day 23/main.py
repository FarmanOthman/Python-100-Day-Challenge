import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle crossing")
screen.tracer(0)

tim = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()


while not tim.is_at_finish_line():
    time.sleep(0.1)
    screen.listen()
    screen.onkey(tim.move, "Up")
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    
    for car in car_manager.all_cars:
        if tim.distance(car) < 20:
            screen.bye()  

    if tim.is_at_finish_line():
        tim.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
