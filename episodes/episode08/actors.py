"""
Icy Tower in Python & Turtle Graphics | @TheWannabeCoder
--------------------------------------------------------
actors.py — Core game entities for the Icy Tower game

This module defines the main player in the game.

Each actor is built on top of the Turtle class and includes logic for
positioning, movement, and interaction within the game environment.
"""

import turtle
import os
from constants import (ACCELERATION, TURN_FACTOR, JUMP_DISTANCE,
                       JUMP_FACTOR, GRAVITY, FRICTION, 
                       PLAYER_PIXEL_SIZE, PLAT_PIXEL_SIZE, 
                       WALL_BOUNCE_FACTOR, WALL_PIXEL_SIZE,
                       MAX_SPEED, ROTATION_SPEED)


class Actor(turtle.Turtle):
    "General Actor Blueprint"
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()


class Player(Actor):
    "Player"

    def __init__(self, start_x, start_y, platforms, walls):
        super().__init__()
        # Define a list of player rotation shapes
        self.rotation_sprites = [
            "player.gif",        # 0°  (front-facing)
            "player_45r.gif",    # 45° right
            "player_90r.gif",    # 90° right (side)
            "player_135r.gif",   # 135° right (back-side)
            "player_180.gif",    # 180° (back)
            "player_135l.gif",   # 225° (back-side left)
            "player_90l.gif",    # 270° (side left)
            "player_45l.gif",    # 315° (front-side left)
        ]
        # Set initial shape
        self.shape(self.rotation_sprites[0])
        # Map keyboard keys to boolean values
        self.keys = {
            "right": False,
            "left": False,
            "space": False
        }
        self.goto(start_x, start_y)
        # Get positional coordinates of platforms & walls
        self.platforms = platforms
        self.walls = walls
        # Player Attributes
        self.can_jump = True
        self.dx = 0
        self.dy = 0
        self.next_x = self.xcor() + self.dx
        self.next_y = self.ycor() + self.dy
        self.scroll_active = False
        self.scroll_speed = 1
        self.scroll_speed_threshold = 3000
        self.highest_floor = 0
        self.last_dy = 0
        self.rotation_angle = 0
        self.spin_dir = 1

    def go_right(self):
        "Pressing Right Key"
        self.keys["right"] = True

    def go_left(self):
        "Pressing Left Key"
        self.keys["left"] = True

    def stop_right(self):
        "Releasing Right Key"
        self.keys["right"] = False

    def stop_left(self):
        "Releasing Left Key"
        self.keys["left"] = False

    def press_space(self):
        "Pressing Jump Key"
        self.keys["space"] = True

    def release_space(self):
        "Releasing Jump Key"
        self.keys["space"] = False

    def keyboard_input(self):
        "Keyboard Mapping"
        # Left / Right
        if self.keys["right"]:
            if self.dx < 0:
                self.dx += ACCELERATION * TURN_FACTOR
            else:
                self.dx += ACCELERATION
        if self.keys["left"]:
            if self.dx > 0:
                self.dx -= ACCELERATION * TURN_FACTOR
            else:
                self.dx -= ACCELERATION
        # Space
        if self.keys["space"] and self.can_jump:
            os.system("aplay jump.wav &")
            boost = abs(self.dx) * JUMP_FACTOR
            self.dy = JUMP_DISTANCE + boost
            self.can_jump = False
            # Determine the direction of spin based on movement direction
            self.spin_dir = 1 if self.dx >= 0 else -1

    def apply_physics(self):
        "Game Physics"
        # Gravity - only when not on platforms
        if not self.can_jump:
            self.dy -= GRAVITY
        # Friction - only when keys are not pressed and on platforms
        if (
            not self.keys["right"] and not
            self.keys["left"] and
            self.can_jump
        ):
            self.dx *= FRICTION
        # Air Friction
        if not self.can_jump:
            self.dx *= 0.98

    def check_collisions(self):
        "Platforms & Walls Collision"
        # Wall Collisions
        player_right = self.next_x + PLAYER_PIXEL_SIZE / 2
        player_left = self.next_x - PLAYER_PIXEL_SIZE / 2
        for wall in self.walls:
            wall_left = wall.xcor() - WALL_PIXEL_SIZE / 2
            wall_right = wall.xcor() + WALL_PIXEL_SIZE / 2
            # Colliding with left side of wall while moving right
            if player_right > wall_left and self.xcor() < wall.xcor():
                self.setx(wall_left - PLAYER_PIXEL_SIZE / 2)
                self.dx = -abs(self.dx) * WALL_BOUNCE_FACTOR
                self.dy += abs(self.dx) * WALL_BOUNCE_FACTOR
            # Colliding with right side of wall while moving left 
            elif player_left < wall_right and self.xcor() > wall.xcor():
                self.setx(wall_right + PLAYER_PIXEL_SIZE / 2)
                self.dx = abs(self.dx) * WALL_BOUNCE_FACTOR
                self.dy += abs(self.dx) * WALL_BOUNCE_FACTOR

        # Platform Collisions:
        for plat in self.platforms:
            plat_top = plat.ycor() + PLAT_PIXEL_SIZE / 2
            plat_right = plat.xcor() + plat.length * 10
            plat_left = plat.xcor() - plat.length * 10
            player_bottom = self.ycor() - PLAYER_PIXEL_SIZE / 2
            # Conditions to land:
            # - Falling down (dy <= 0)
            # - Player is horizontally within platform bounds (with tolerance)
            # - Player's feet are close enough to the top of the platform
            if (
                self.dy <= 0 and
                plat_left - PLAYER_PIXEL_SIZE / 3 <= self.xcor() <= plat_right + PLAYER_PIXEL_SIZE / 3 and
                abs(player_bottom - plat_top) <= max(1, -self.dy)
            ):
                self.sety(plat_top + PLAYER_PIXEL_SIZE / 2)
                self.dy = 0
                self.can_jump = True
                # Stop checking after landing
                return
        # Player is in the air (not on any platform)
        self.can_jump = False

    def move(self):
        "Movement"
        # Calculate next x, y position
        self.next_x = self.xcor() + self.dx
        self.next_y = self.ycor() + self.dy
        # Set speed to 0
        if abs(self.dx) < 0.1:
            self.dx = 0
        # Set new player position
        self.goto(self.next_x, self.next_y)
        # Max Speed:
        if self.dx > MAX_SPEED:
            self.dx = MAX_SPEED
        elif self.dx < - MAX_SPEED:
            self.dx = -MAX_SPEED

    def update(self):
        """
        Updates the player's state for the current frame.
        
        Handles:
        - Input processing
        - Physics
        - Collision detection
        - Movement
        - Airborne spin animation
        - Grounded sprite reset
        """
        self.keyboard_input()
        self.apply_physics()
        self.check_collisions()
        self.move()
        # Play jump sound when player crosses upward threshold
        if self.last_dy <= 24.5 < self.dy:
            os.system("aplay wohoo.wav &")
        self.last_dy = self.dy
        # While airborne and moving horizontally, animate spin
        if not self.can_jump and self.dx != 0:
            # Increase rotation angle based on spin direction and speed
            # (wrap around using % 360 to keep it between 0 and 359 degrees)
            self.rotation_angle = (
                self.rotation_angle + ROTATION_SPEED * self.spin_dir) % 360
            # Determine the sprite index by dividing the angle into 45° segments
            # (there are 8 sprites for 360°, so 360 / 45 = 8 frames)
            idx = int(self.rotation_angle / 45) % len(self.rotation_sprites)
            # Set the current sprite to match the calculated rotation frame
            self.shape(self.rotation_sprites[idx])

        # once you land, reset and fall back to left/right/straight
        else:
            self.rotation_angle = 0
            if self.dx < 0:
                self.shape("player_left.gif")
            elif self.dx > 0:
                self.shape("player_right.gif")
            else:
                self.shape("player.gif")
