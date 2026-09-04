# Feint-and-Fury
It is an interactive 1v1 textbased combat game. The players faceoff againt an automoted opponent. The game requires resource management, risk management and tactical thinking.

## Features:
* **Dynamic Difficulty:** The game has 3 different difficulty levels which tweak the health, the resources and the power of the attacks delt by the player.
* **Dice-Roll Combat Mechanics:** The game uses dice-roll based combat mechanics which randomise the outcome of an attack. This adds an unpredictable element to the game.
* **Resource Management:** Players get a fixed amount of health and strength boosts at the beginning of a game. The players need to use these limited resources carefully and tactically, making sure that they neither finish them early nor let them go to waste.
* **Modularity:** The entire codebase has been segregated into four discrete modules. Each module does a specific task. This makes the code easy to tweak and easy to maintain.

## Project Structure:
* 'main.py': Orchestrates the primary game loop, state handling, and turn transitions
* 'attacks.py': Contains move sets (Slash, Fireball, Arrow Shot, Thunderbolt) and damage/RNG resolution
* 'inventory.py': Manages potion consumption and player stat boosts
* 'rules.py': Built-in interactive rulebook for player onboarding

## Getting Started:
### Prerequisites
* Python 3.10+ (tested on Python 3.12)

### Running the Game
1. Clone the repository:
   ```bash
   git clone [https://github.com/](https://github.com/)shaunaknar-bip/feint-and-fury.git
   cd feint-and-fury
2. Launch the game:
   ```bash
   python main.py
