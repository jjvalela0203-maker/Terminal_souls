# ⚔️ Terminal Souls

A turn-based combat game played in the terminal, where a Hero battles against an Enemy using different actions and strategies.

---

## 📌 Description

**Terminal Souls** is a simple Python project that simulates a 1 vs 1 combat system.
The player takes control of a Hero and must defeat an Enemy by choosing actions each turn.

The game demonstrates the use of:

* Functions (modular programming)
* Control structures (`while`, `if`)
* User input handling
* File separation and imports

---

## 🎮 Gameplay

Each turn, the player can choose one of the following actions:

1. **Attack** → Deals random damage (10–25)
2. **Heal** → Restores 20 HP (limited potions)
3. **Special Ability** → Deals high damage (30–50) but has a 50% chance to fail

After the player's turn, the Enemy attacks automatically.

The game continues until either the Hero or the Enemy reaches **0 HP**.

---

## 🧱 Project Structure

```
terminal_souls/
│
├── main.py        # Main game loop
├── funciones.py   # Game logic and functions
└── config.py      # Game constants and settings
```

---

## ⚙️ Requirements

* Python 3.x

No external libraries are required (only built-in modules like `random`).

---

## ▶️ How to Run

1. Open a terminal in the project folder
2. Run the following command:

```bash
python main.py
```

---

## 🧠 Key Features

* Turn-based combat system
* Randomized damage system
* Input validation (prevents invalid actions)
* Modular code structure using multiple files
* Simple and clean terminal interface
* Visual health bar system for both hero and enemy

---

## 🚀 Possible Improvements

* Add a visual health bar
* Implement critical hits (10% chance)
* Add enemy AI (healing behavior)
* Let the player choose a name
* Add more abilities or characters

---

## 👤👤 Authors

Juan Jose Varela and Carlos Aponte

---

## 📅 Date

March 2026
