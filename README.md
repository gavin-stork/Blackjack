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

### Run the Game

1. Clone the repository:
   git clone https://github.com/yourusername/blackjack-terminal-game.git
   cd blackjack-terminal-game
2. Run the game
   python blackjack.py

## How to Play
You're dealt two cards, and one dealer card is shown.
Your goal is to reach 21 without going over (bust).
You can choose to:
hit: draw another card
stand: keep your current hand
Aces count as 1 or 11, whichever is more favorable.
Dealer must stand on 17 or higher.
The closest to 21 wins — or it's a tie if scores match.

## Sample Output

========================================
         Welcome to Blackjack!
========================================

Goal: Get as close to 21 as possible without going over.
Rules:
 - Number cards are worth their value (2-10).
 - Face cards (Jack, Queen, King) are worth 10 points.
 - Aces can be worth 1 or 11 points, whichever helps you more.
 - If you are dealt 21, you win immediately!
 - If you go over 21, you bust and lose.
 - Dealer must stand on 17 or higher.
 - If you and dealer have the same total, it's a tie (push).

Dealer visible card:
  - 8 of Hearts

Your hand:
  - King of Spades
  - 7 of Clubs

Your total: 17

Do you want to hit or stand? (h/s): s

You chose to stand at 17.

Dealer flips 9 of Diamonds
Dealer's hand:
  - 8 of Hearts
  - 9 of Diamonds

Dealer's total: 17

Dealer stands at 17.

========================================
              Final Result
========================================
Your final total: 17
Dealer final total: 17

It's a push (tie)!
