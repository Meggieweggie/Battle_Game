# Battle Game

A simple text-based RPG battle game where players choose a character to fight against a dragon.

## Game Overview

Players select from three character classes, each with unique stats, and engage in turn-based combat with a dragon until one side is defeated.

## Characters

| Character | HP  | Damage |
|-----------|-----|--------|
| Wizard    | 70  | 150    |
| Elf       | 100 | 100    |
| Human     | 150 | 20     |

**Dragon Stats:** 300 HP, 50 Damage

## How to Play

1. Run the game: `python3 BattleGame.py`
2. Choose your character (1-3)
3. Battle proceeds automatically until victory or defeat

## Requirements

- Python 3.x

## Installation

```bash
git clone <repository-url>
cd Battle_Game
python3 BattleGame.py
```

## Game Mechanics

- Turn-based combat
- Player attacks first each round
- Battle continues until either player or dragon reaches 0 HP
- No healing or special abilities