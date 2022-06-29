from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.shapesize(stretch_wid= 1, stretch_len= 2)
        self.goto(300, random.randint(-300, 300))

    def move(self, vehicle_points):
        self.forward(MOVE_INCREMENT)
        if self.xcor() <= -300:
            self.goto(x=300, y= random.choice(vehicle_points))

    def detect_collision(self, turtle_ycor):
        if abs((turtle_ycor - self.ycor())) < 20 and self.xcor() ==0:

            return True
        else:
            pass

