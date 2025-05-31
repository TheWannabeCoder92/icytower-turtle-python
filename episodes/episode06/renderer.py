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
from constants import *


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
        self.showturtle()
        self.shape("square")
        self.shapesize(stretch_wid=WALL_SHAPE_HEIGHT * 100000,
        stretch_len=WALL_SHAPE_SIZE)
        self.pencolor("white")
        self.fillcolor("slategray")
        self.goto(x, 0)


class Platform(GeneralPen):
    "Platforms"
    def __init__(self, plat_x, plat_y, length):
        super().__init__()
        self.showturtle()
        self.shape("square")
        self.length = length
        self.shapesize(stretch_wid=PLAT_SHAPE_SIZE, stretch_len=self.length)
        self.pencolor("white")
        self.fillcolor("saddlebrown")
        self.goto(plat_x, plat_y)
        self.floor_num = 0

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



