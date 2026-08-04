# 🔢 Java Guess The Number Game

**Version:** v1.0 (Console Edition)

A classic console-based number guessing game built to solidify my understanding of Java's control flow and game loop mechanics. The program generates a random number between 1 and 100, challenging the player to find it.

### ⚙️ Core Mechanics & Features
* **Randomization:** Utilizes the `java.util.Random` class to generate the target number.
* **Input Handling:** Captures user guesses in real-time via `java.util.Scanner`.
* **Game Loop:** Implements an infinite `while(true)` loop that only breaks when the correct condition (winning) is met.
* **Validation:** Includes boundary checks to notify the user if their guess is less than 0 or greater than 100.

### 🚀 Upcoming Updates (v2.0)
* **Attempt Counter:** Tracking how many tries it takes to win.
* **Smart Hints:** Giving the user "Higher!" or "Lower!" clues instead of just saying "Wrong".
* **Multiplayer Mode:** Adding a turn-based system for two players.
