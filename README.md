# Blackjack Terminal Game 🎲🃏

A terminal-based Blackjack game built in Python using `asyncio`. Play against a dealer with realistic card handling, smart Ace evaluation (1 or 11), and a clean, readable user interface.

---

## Features

- ✅ Full 52-card deck with random shuffle  
- 🧠 Dynamic Ace values (1 or 11)  
- 💻 Terminal-friendly UI — no external libraries  
- 🤖 Dealer logic that stands on 17 or higher  
- ❌ Detects busts and handles ties ("push")  
- ⏱ Uses `asyncio` for smoother game flow  

---

## Getting Started

### Requirements

- Python 3.7 or higher

### Running the Game

```bash
git clone https://github.com/gavin-stork/blackjack.git
cd blackjack
python blackjack.py
```

## How to Play
- You're dealt two cards, and one dealer card is shown.
- Your goal is to reach 21 without going over (bust).
- You can choose to:
  - hit: draw another card
  - stand: keep your current hand
- Aces count as 1 or 11, whichever is more favorable.
- Dealer must stand on 17 or higher.
- The closest to 21 wins — or it's a tie if scores match.

## Sample Output
<img width="451" height="884" alt="image" src="https://github.com/user-attachments/assets/6449dc61-f566-428c-a089-868d0dc80165" />

---

## Author
Gavin Stork


