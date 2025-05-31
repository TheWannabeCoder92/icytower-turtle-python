"""
Icy Tower in Python & Turtle Graphics | @TheWannabeCoder
--------------------------------------------------------
This script is the main entry point for the game.
It initializes the screen, creates the player and platform objects,
and starts the main game loop for real-time updates.    

It handles:
- Screen setup and event bindings
- Initialization of game objects (player, platforms, UI)
- The core game loop that updates the screen
"""

import turtle
import random
from constants import *
from renderer import Wall, Platform
from actors import Player


def init_screen():
    "Initialize Main Game Screen"
    screen = turtle.Screen()
    screen.tracer(0)
    screen.title("Icy Tower in Python | @TheWannabeCoder")
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")
    return screen


def bind_controls(screen, player):
    "Keyboard & Mouse Bindings"
    screen.listen()
    screen.onkeypress(player.go_right, "Right")
    screen.onkeyrelease(player.stop_right, "Right")
    screen.onkeypress(player.go_left, "Left")
    screen.onkeyrelease(player.stop_left, "Left")
    screen.onkeypress(player.press_space, "space")
    screen.onkeyrelease(player.release_space, "space")

def game_loop(screen, walls, platforms, player):
    """
    Main game loop that handles real-time updates.

    This loop runs continuously using the screen's `ontimer` method to:
    - Update player movement
    - Scroll the screen upward as the player climbs
    - Update the UI (score, lives, etc.)

    It ensures smooth gameplay by updating the game state at regular intervals.
    """
    # Update player's movement
    # Keyboard Input, Physics, Collision, Movement
    player.update()

   # Update screen animation
    screen.update()
    # Recall the game loop function every 16ms
    screen.ontimer(lambda: game_loop(
        screen, walls, platforms, player), 1000 // 60)


def main():
    """
    Initializes and starts the Icy Tower game.

    This function sets up the screen, creates the player and initial platforms,
    binds user input to control functions, and starts the main game loop which
    handles real-time screen updates.
    """
    # Create Screen
    screen = init_screen()
    # Create Walls
    right_wall = Wall(SCREEN_WIDTH // 2 - WALL_PIXEL_SIZE)
    left_wall = Wall(-SCREEN_WIDTH // 2 + WALL_PIXEL_SIZE)
    walls = [right_wall, left_wall]
    # Create Platforms
    # Floor
    floor = Platform(0, GROUND_Y, FLOOR_SHAPE_LENGTH)
    platforms = [floor]
    for i in range(30):
        # Choose platform length and get the range in which we can place it to not go off screen
        length = random.randint(6, 12)
        max_x = (FLOOR_PIXEL_LENGTH - length * 20) / 2
        plat_x = random.randint(-int(max_x), int(max_x))
        plat_y = GROUND_Y + (i + 1) * (PLAYER_PIXEL_SIZE +
                                       PLAT_PIXEL_SIZE + SCREEN_MARGIN)
        # Create the platform
        platform = Platform(plat_x, plat_y, length)
        # Set the platform count
        platform.floor_num = i + 1
        platforms.append(platform)
    # Create Player
    start_x = 0
    start_y = PLAYER_START_Y
    player = Player(start_x, start_y, platforms, walls)
    # Keyboard Bindings:
    bind_controls(screen, player)
    # Game Loop: (Real-Time Updates)
    game_loop(screen, walls, platforms, player)
    # Keep window open:
    screen.mainloop()


# Open only if run directly:
if __name__ == "__main__":
    main()
