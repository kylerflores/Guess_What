# Guess What? - Pass and Play (Python)
A Python implementation of the classic board game Guess Who?, designed as a pass-and-play experience for two players. Players take turns asking yes/no questions to guess their opponent's mystery character before the other player does.

## Features
- Two-player pass-and-play: Players share the same device, taking turns.
- Text-based interface: Simple console-based interaction.
- Character selection: Each player gets to choose their mystery characters at the start of each round.
- Turn-based gameplay: Players alternate asking questions to eliminate candidates.

## How to Play
1. Setup:
    - Each player selects a mystery character.
    - Players take turns passing the device back and forth.
2. Gameplay:
    - On your turn, ask a yes/no question (e.g., "Does your person wear glasses?") to narrow down the options.
    - Based on the answer, eliminate characters that don’t match the criteria.
    - Use logic to guess your opponent’s character before they guess yours!
3. Winning:
    - The first player to correctly guess the opponent’s mystery character wins.

## Requirements  
- Python 3.6+ (or 3.8+ recommended)

## How to Run
1. Clone or download this repository.
2. Navigate to the project directory in your terminal.
3. Run the game: python guess_what.py
4. Follow the on-screen instructions to play.

## Customization (Coming Soon...)
- Create your own custom game boards by uploading your own photos

## Future Improvements
- Implement a round and point system
- Add a PyQt GUI
- Allow users to create and save custom game boards
- Implement a single-player mode against AI.