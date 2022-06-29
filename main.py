import time, random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.title("TURTLE CROSSING!")
screen.setup(width=600, height=600)
screen.tracer(0)

tortoise = Player()
level = Scoreboard()
car = CarManager()
screen.listen()

screen.onkey(tortoise.move, "Up")

#Initialize the cars

VEHICLE_POINTS = [-230, -200, -170, -150, -120, -90, -60, -30, 0,
                  30, 60, 90, 120, 150, 170, 200, 230]
vehicles = []

for n in VEHICLE_POINTS:
    if random.randint(0, 100) >= 50:
        new_vehicle = CarManager()
        new_vehicle.goto(random.randint(-230, 300), n)
        vehicles.append(new_vehicle)
    else:
        pass

game_is_on = True
while game_is_on:
    time.sleep(level.move_speed)

    for n in vehicles:
        n.move(VEHICLE_POINTS)
        if n.detect_collision(tortoise.ycor()):
            level.game_over()
            game_is_on = False
    screen.update()

    if tortoise.ycor() >= 280:
        tortoise.reset()
        level.level_up()
    else:
        pass

screen.exitonclick()