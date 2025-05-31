# 🧍 Episode 3 – Player Setup & Keyboard Controls

In this episode, we add the **player character** and make it controllable with the keyboard!

We introduce a new file called `actors.py` to manage game actors (starting with the player), and we wire up keyboard controls to move the player left, right, and prepare for jumping.

---

## 🛠️ What We Cover

- ✅ Creating a `Player` class in `actors.py`.
- ✅ Tracking keyboard input (left, right, jump).
- ✅ Updating the game loop to handle player movement.
- ✅ Ensuring smooth movement with velocity-based updates.

---

## ▶️ How to Run

Make sure you have Python 3 installed. Then run:

```bash
python main.py
```

A player turtle should now appear, and you can move it left or right using the arrow keys, and jump using the space key!

---

## 📁 Files Included

- `main.py` – Runs the game loop and listens for keyboard input.
- `constants.py` – Updated with player speed and movement constants.
- `renderer.py` – Still responsible for rendering the walls and platforms.
- `actors.py` – New! Defines the `Player` class and handles movement logic.

---

In the next episode, we’ll introduce **gravity and collision detection** to make the player land on platforms and simulate real jumping physics!
