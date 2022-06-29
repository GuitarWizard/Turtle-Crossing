from turtle import Turtle, Screen

FONT = ("Times New Roman", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(-240, 250)
        self.write(f" Level: {self.level}", False, "center", FONT)
        self.move_speed = 0.1

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f" Level: {self.level}", False, "center", FONT)
        self.move_speed *= 0.9

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER! Final Level: {self.level}", False, "center", FONT)
