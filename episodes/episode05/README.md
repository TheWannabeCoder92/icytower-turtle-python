# 📜 Episode 5 – Screen Scrolling & Platform Recycling

In this episode, we add vertical scrolling to simulate climbing — just like in the real Icy Tower!

As the player jumps higher, the entire environment scrolls down, and platforms that leave the screen get recycled back to the top.

---

## 🛠️ What We Cover

- ✅ Implementing vertical screen scrolling based on player height.
- ✅ Moving all platforms and background elements downward as the player ascends.
- ✅ Recycling platforms that go off-screen and repositioning them above.

---

## ▶️ How to Run

Make sure you have Python 3 installed. Then run:

```bash
python main.py
```
You should now see the entire screen scroll downward as you climb, with platforms continuously spawning from the top to keep the action going!

---

## 📁 Files Included

- `main.py` – Handles the main game loop and scrolling logic.
- `constants.py` – May include new values for scroll thresholds or speed.
- `renderer.py` – Manages wall and platform visuals during scroll.
- `actors.py` – Updated with logic to trigger and respond to screen scrolling.

---

In the next episode, we’ll create a **score system** that tracks how high you’ve climbed!
