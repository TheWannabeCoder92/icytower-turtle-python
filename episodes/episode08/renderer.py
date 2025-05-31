"""
Icy Tower in Python & Turtle Graphics | @TheWannabeCoder
--------------------------------------------------------
renderer.py — Rendering classes for the Icy Tower game (Turtle Graphics)

This module defines all visual components of the game, including:
- Platform rendering
- Score display
- Decorative effects

Each renderer class extends the Turtle module and is responsible
for drawing specific game elements on screen.
"""

import turtle
import random
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, GRAVITY


class GeneralPen(turtle.Turtle):
    "General Pen Blueprint"
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()


class Wall(GeneralPen):
    "Walls"
    def __init__(self, x):
        super().__init__()
        self.goto(x, 0)


class Platform(GeneralPen):
    "Platforms"
    def __init__(self, plat_x, plat_y, length):
        super().__init__()
        self.showturtle()
        self.length = length
        self.goto(plat_x, plat_y)
        self.floor_num = 0
        if self.length == 12:
            self.shape("plat_12.gif")
        elif self.length == 11:
            self.shape("plat_11.gif")
        elif self.length == 10:
            self.shape("plat_10.gif")
        elif self.length == 9:
            self.shape("plat_9.gif")
        elif self.length == 8:
            self.shape("plat_8.gif")
        elif self.length == 7:
            self.shape("plat_7.gif")
        elif self.length == 6:
            self.shape("plat_6.gif")
        else:
            self.shape("floor.gif")


class Score(GeneralPen):
    "Score Display"
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(-SCREEN_WIDTH//2 + 10, SCREEN_HEIGHT//2 - 60)
        self.pencolor("ghostwhite")
        self.write(f"Score: {self.score}", align="left",
                   font=("Courier", 32, "bold"))

    def update(self, new_score):
        "Update Score"
        self.score = new_score
        self.clear()
        self.write(f"Score: {self.score}", align="left",
                   font=("Courier", 32, "bold"))

    def game_over(self):
        "Game Over"
        self.goto(0, -50)
        self.color("crimson")
        self.write(f"Game Over!\nFinal Score: {self.score}", align="center", font=(
            "Courier", 50, "bold"))


class Star(GeneralPen):
    "Stars"
    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.shapesize(0.5)
        # pick a random bright color
        self.color(random.choice(
            ["yellow", "cyan", "magenta", "orange", "white", "lightgreen", "red", "indigo"]))
        self.goto(x, y)
        self.setheading(random.randint(0, 360))
        self.showturtle()
        # drop speed
        self.dy = 0
        self.angle = self.heading()

    def update(self):
        "Stars Movement"
        self.dy -= GRAVITY
        self.angle += 15
        self.setheading(self.angle)
        self.goto(self.xcor(), self.ycor() + self.dy)
