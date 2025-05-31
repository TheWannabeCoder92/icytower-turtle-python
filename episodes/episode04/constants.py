"""
Icy Tower in Python & Turtle Graphics | @TheWannabeCoder
--------------------------------------------------------
constants.py — Configuration values for the Icy Tower game

This module defines all global constants used throughout the game,
including screen dimensions, object sizes, colors, physics values,
scrolling speeds, and scoring thresholds.

Centralizing constants here improves readability and makes it easier
to tweak gameplay balance or visual settings.
"""

# Screen Parameters
SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 1000
SCREEN_MARGIN = 20
# Wall Parameters
WALL_PIXEL_SIZE = 30
WALL_SHAPE_SIZE = WALL_PIXEL_SIZE / 20 
WALL_SHAPE_HEIGHT = SCREEN_HEIGHT / 20
# Platform Parameters
PLAT_PIXEL_SIZE = 30
PLAT_SHAPE_SIZE = PLAT_PIXEL_SIZE / 20
FLOOR_PIXEL_LENGTH = SCREEN_WIDTH - 2 * (WALL_PIXEL_SIZE + SCREEN_MARGIN)
FLOOR_SHAPE_LENGTH = FLOOR_PIXEL_LENGTH / 20
GROUND_Y = -SCREEN_HEIGHT / 2 + 50
# Player Parameters
PLAYER_PIXEL_SIZE = 40
PLAYER_SHAPE_SIZE = PLAYER_PIXEL_SIZE / 20
PLAYER_START_Y = GROUND_Y + (PLAT_PIXEL_SIZE + PLAYER_PIXEL_SIZE) / 2
# Game Physics Parameters
GRAVITY = 1
FRICTION = 0.9
JUMP_DISTANCE = 14
JUMP_FACTOR = 0.75
WALL_BOUNCE_FACTOR = 0.75
ACCELERATION = 0.5
MAX_SPEED = 15
TURN_FACTOR = 5
ROTATION_SPEED = 10
