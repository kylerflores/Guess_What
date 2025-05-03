"""This is where it all happens"""
from src.model import player
from . import guess_what_console as console

def main():
    """main function"""
    # Get player names from input
    p1_name = input("Enter name for Player 1: ").strip() or "Player 1" # Default if empty
    p2_name = input("Enter name for Player 2: ").strip() or "Player 2" # Default if empty
    p1 = player.Player(p1_name)
    p2 = player.Player(p2_name)
    mode : chr = 'x'
    while (mode != 'c' and mode != 'u'):
        mode = input("Enter 'c' for console mode or 'u' for UI mode: ").strip()
    if mode == 'c':
        # game = console.GuessWhatConsole(p1, p2)
        pass
    else:
        # game = gui.GuessWhatGui(p1, p2)
        print(r"""
        [Sorry, UI mode is not available yet]
                                                 \ / _
                                             ___,,,
                                             \_[o o]
            Get back to work!                C\  _\/
                    /                     _____),_/__
               ________                  /     \/   /
             _|       .|                /      o   /
            | |       .|               /          /
             \|       .|              /          /
              |________|             /_        \/
              __|___|__             _//\        \ 
        _____|_________|____       \  \ \        \ 
                           _|       ///  \        \ 
                          |               \       /
                          |               /      /
                          |              /      /
        ________________  |             /__    /_
                     ...|_|.............. /______\.......
        
        [For now, please enjoy the console mode!]""")
    game = console.GuessWhatConsole(p1, p2)
    game.play()
