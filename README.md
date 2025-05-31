# Icy Tower in Python ❄️🕹️

This is a beginner-friendly **Icy Tower–style platformer** built using Python's Turtle Graphics module.

The code is part of a full YouTube tutorial series, where we build the game step by step — covering everything from movement physics and wall bouncing to infinite vertical scrolling, UI, and visual effects.

## 🎥 Watch the Tutorial Series

YouTube Playlist: [Icy Tower in Python - Full Tutorial Series](https://www.youtube.com/playlist?list=PL1XCNNzXQuPME9orzlJcHu7NpbsNbQ5Du)

---

## 📚 Table of Contents

Use the links below to access the code for each episode:

1. [Episode 1 – Project & Screen Setup](https://github.com/TheWannabeCoder92/icytower-turtle-python/tree/main/episodes/episode01)
2. [Episode 2 – Wall & Platform Rendering](https://github.com/TheWannabeCoder92/icytower-turtle-python/tree/main/episodes/episode02)
3. [Episode 3 – Player Movement & Keyboard Input](https://github.com/TheWannabeCoder92/icytower-turtle-python/tree/main/episodes/episode03)
4. [Episode 4 – Physics & Collision](https://github.com/TheWannabeCoder92/icytower-turtle-python/tree/main/episodes/episode04)
5. [Episode 5 – Screen Scrolling & Platform Recycling](https://github.com/TheWannabeCoder92/icytower-turtle-python/tree/main/episodes/episode05)
6. [Episode 6 – Score Tracking & Game Over](https://github.com/TheWannabeCoder92/icytower-turtle-python/tree/main/episodes/episode06)
7. [Episode 7 – Graphics & Audio](https://github.com/TheWannabeCoder92/icytower-turtle-python/tree/main/episodes/episode07)

📂 [View Full Project Structure](#-project-structure)

---

Follow along to:
- Learn how to simulate physics-based platformer gameplay
- Use Turtle Graphics to draw, animate, and update game elements in real time
- Implement scoring systems, infinite scrolling, and jump effects
- Polish your game with sprite animation and audio feedback

## 📁 Project Structure

```
icytower-turtle-python/
│
├── README.md
├── LICENSE
├── .gitignore
├── media/
│   └── final_game.mp4
│
└── episodes/
    ├── episode01/       # Project & Screen Setup
    │   ├── README.md
    │   ├── constants.py
    │   └── main.py
    │
    ├── episode02/       # Wall & Platform Rendering
    │   ├── README.md
    │   ├── constants.py
    │   ├── main.py
    │   └── renderer.py
    │
    ├── episode03/       # Player Movement & Keyboard Input
    │   ├── README.md
    │   ├── actors.py
    │   ├── constants.py
    │   ├── main.py
    │   └── renderer.py
    │
    ├── episode04/       # Physics & Collision
    │   ├── README.md
    │   ├── actors.py
    │   ├── constants.py
    │   ├── main.py
    │   └── renderer.py
    │
    ├── episode05/       # Screen Scrolling & Platform Recycling
    │   ├── README.md
    │   ├── actors.py
    │   ├── constants.py
    │   ├── main.py
    │   └── renderer.py
    │
    ├── episode06/       # Score Tracking & Game Over
    │   ├── README.md
    │   ├── actors.py
    │   ├── constants.py
    │   ├── main.py
    │   └── renderer.py
    │
    └── episode07/       # Final Game – Graphics, Audio & Effects
        ├── README.md
        ├── actors.py
        ├── background.gif
        ├── constants.py
        ├── floor.gif
        ├── jump.wav
        ├── main.py
        ├── plat_6.gif
        ├── plat_7.gif
        ├── plat_7.png
        ├── plat_8.gif
        ├── plat_8.png
        ├── plat_9.gif
        ├── plat_10.gif
        ├── plat_11.gif
        ├── plat_12.gif
        ├── player.gif
        ├── player_45l.gif
        ├── player_45r.gif
        ├── player_90l.gif
        ├── player_90r.gif
        ├── player_135l.gif
        ├── player_135r.gif
        ├── player_180.gif
        ├── player_left.gif
        ├── player_right.gif
        ├── renderer.py
        └── wohoo.wav
```

📦 **Note:** 
- `episode07/` contains the final version of the complete game.  
- Sound effects are played using `aplay` (Linux) — you may need to adjust the command for Windows `winsound`  or macOS `afplay`.  
- Game physics and scoring logic can all be tweaked in `constants.py`.

## 📋 Requirements

No external libraries needed – just Python 3.x.

Make sure `turtle` is available (it's included with standard Python installs).

## ▶️ How to Run

```bash
python main.py
```

The game window will open, and you can start playing Icy Tower using the Right & Left arrow keys to move and Space key to jump.

## 📌 About the Creator

Created by TheWannabeCoder  
Making simple, hands-on Python tutorials for beginners.  
YouTube: [@TheWannabeCoder](https://www.youtube.com/@TheWannabeCoder)

## 📜 License

This project is licensed under the MIT License.
