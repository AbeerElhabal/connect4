# Connect 4 - AI Game 

A terminal-based Connect 4 game with an AI opponent using the **Minimax Algorithm**.

---

##  Developer
- Abeer

---

##  Project Structure

| File | Description |
|------|-------------|
| `board.py` | Board creation, display, and win detection |
| `player.py` | Human and AI player classes |
| `minimax.py` | Minimax algorithm and board scoring |
| `game.py` | Game flow and turn management |
| `main.py` | Entry point of the game |

---

##  How to Run

```bash
python main.py
```

---

##  Game Modes

- **Human vs AI** → Play against the Minimax AI
- **Human vs Human** → Play with a friend

---

##  AI Strategy

The AI uses the **Minimax Algorithm** with:
- Depth of 5 moves ahead
- Board scoring based on center control and piece patterns
- Random selection between equally scored moves

---

##  Course Info

- **Course:** Artificial Intelligence 2025/2026
- **Project:** Adversarial Search - Connect 4
