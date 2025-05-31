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
from renderer import Wall, Platform, Score
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


def scroll_world(walls, platforms, player):
    """
    Scrolls the game world upward and recycles platforms.

    Moves all game elements downward by the given delta `dy`, creating the illusion 
    of the player climbing. Any platforms that move off-screen at the bottom are removed 
    and new ones are generated at the top, keeping the number of platforms constant.
    """
    # 1) Start scrolling once the player rises above threshold
    if not player.scroll_active and player.ycor() > SCROLL_THRESHOLD:
        player.scroll_active = True
    if player.scroll_active:
        # pick fast or slow speed
        speed = FAST_SCROLL_SPEED if player.ycor() > FAST_SCROLL_Y else player.scroll_speed
        # move the world down — platforms, walls & player
        for obj in platforms + walls + [player]:
            obj.sety(obj.ycor() - speed)
    # 2) Recycle platforms once they’ve fully fallen off-screen
    # Find the current highest platform's Y position
    top_y = max(plat.ycor() for plat in platforms)
    # Calculate next available floor number
    next_floor = max(plat.floor_num for plat in platforms) + 1
    for plat in platforms:
        top_edge = plat.ycor() + PLAT_PIXEL_SIZE/2
        if top_edge < -SCREEN_HEIGHT / 2:
            # Calculate new y-position
            gap = PLAYER_PIXEL_SIZE + PLAT_PIXEL_SIZE + SCREEN_MARGIN
            new_y = top_y + gap
            # Assign next floor number
            plat.floor_num = next_floor
            next_floor += 1
            # Randomly choose new x-position
            max_x = (FLOOR_PIXEL_LENGTH - plat.length * 20) / 2
            new_x = random.randint(-int(max_x), int(max_x))
            plat.goto(new_x, new_y)


def game_loop(screen, walls, platforms, player, score_display):
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
    # Scroll world and recycle off screen platforms
    scroll_world(walls, platforms, player)
    # Scoring
    # ─── floor-based scoring ───
    # Get y-position of the player's feet (bottom)
    feet_y = player.ycor() - PLAYER_PIXEL_SIZE/2
    # pick platforms whose top edge is at or below your feet
    candidates = [
        plat for plat in platforms
        if plat.ycor() + PLAT_PIXEL_SIZE/2 <= feet_y
    ]
    # Pick the highest platform based on floor number
    if candidates:
        top_plat = max(candidates, key=lambda p: p.floor_num)
        # If this is a new highest floor, update score and player state
        if top_plat.floor_num > player.highest_floor:
            player.highest_floor = top_plat.floor_num
            score_display.score = top_plat.floor_num * 100
    # Increase scroll speed every 3000 points (difficulty scaling)
    if score_display.score >= player.scroll_speed_threshold and player.scroll_speed < MAX_SCROLL_SPEED:
        player.scroll_speed += 1
        player.scroll_speed_threshold += 3000
    # Update score display on screen in real-time
    score_display.update(score_display.score)
    # Game over if the player's head drop below screen window:
    if player.ycor() + PLAYER_PIXEL_SIZE / 2 < -SCREEN_HEIGHT / 2:
        score_display.clear()
        score_display.game_over()
        screen.ontimer(screen.bye, 3000)
        # Stop the game loop
        return
   # Update screen animation
    screen.update()
    # Recall the game loop function every 16ms
    screen.ontimer(lambda: game_loop(
        screen, walls, platforms, player, score_display), 1000 // 60)


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
    # Create Score Display
    score_display = Score()
    # Keyboard Bindings:
    bind_controls(screen, player)
    # Game Loop: (Real-Time Updates)
    game_loop(screen, walls, platforms, player, score_display)
    # Keep window open:
    screen.mainloop()


# Open only if run directly:
if __name__ == "__main__":
    main()
