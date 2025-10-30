# Survival Game

## Description
Survival game set in an abandoned city. The player must manage resources, explore the environment, and survive against unpredictable events during 60 days.

## Requirement 
In order to play this game in the best conditions, python 3.10 or newer should be installed. 

[Link to the python download page](https://www.python.org/downloads/)

## Features
- **Player Stats Management**: Track energy, hunger, and thirst levels.
- **Exploration**: Discover the environment and gather resources to survive.
- **Random Events**: Handle unexpected events that impact survival.
- **Save System**: Save and load player progress.
- **JSON Data Storage**: Save game data in `data/saves/saves.json`.

## Project Structure
```plaintext
survival_game/
├── data/
│   └── saves/
│       └── saves.json          # Game save files
├── game/
│   ├── CLI.py                  # Command-line interface for the game
│   ├── daily_event.py          # Daily events logic
│   ├── game_loop.py            # Main game loop
│   └── player.py               # Player management
├── utils/
│   ├── gauges.py               # Player stats (health, hunger, thirst)
│   └── save_handler.py         # Save and load game data
├── main.py                     # Entry point for the game
└── README.md                   # Project documentation
```

## Environment Variables
- Path to the save file `data/saves/saves.json`.

## Start the Game
```bash
python main.py
```
The game starts in the terminal, displaying available actions for the player.

## Versions
- 1.0 - Initial Release (30/10/2025)

## Technologies
<img src="https://img.shields.io/badge/Python-5E5C5C?style=for-the-badge&logo=python&logoColor=whi" alt="Python logo">
<br>
<img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white" alt="JSON logo">


## Author
Noah CHARRIN--BOURRAT  
Raphaël BONNET 

## Links
- [GitHub Repository](https://github.com/cbnoah/survival_game)