"""This class represents the collection of all characters available in the game"""

class GameBoard:
    """
    This class represents the playing board keeping track of:
        - the selected character
        - character dictionary
    
    Attributes:
        chosen (character): The character that the player chooses for the current round.
        character_dict (str : character): dictionary of characters
        num_flipped (int): stores the number of characters flipped on the board
        
    """
    def __init__(self, character_dict):
        """
        Initializes a new instance of a game board.

        Args:
            character_dict (str : character): dictionary of characters
        """
        self.chosen = None
        self.character_dict = character_dict.copy()
        self.num_unflipped = len(character_dict)

    def chose_round_character(self, chosen):
        """
        Args:
            chosen (character): The character that the player chooses for the current round
        """
        self.chosen = chosen

    def reset_board(self):
        """
        resets the game boards by:
            - unflipping all characters
            - reseting the num_flipped
            - reseting the chosen character
        """
        for i in self.character_dict:
            self.character_dict[i].flipped = False
        self.num_unflipped = len(self.character_dict)
        self.chosen = None

    def flip_character(self, character_id):
        """
        flips or unflips a given character

        Args:
            character_id (str) : ID of the character we want to flip
        """
        curr_character = self.character_dict[character_id]
        if curr_character.flipped:
            self.num_unflipped += 1
        else:
            self.num_unflipped -= 1
        curr_character.flip()

    def is_flipped(self, character_id):
        """
        returns whether or not the charcter is flipped

        Args:
            character_id (str) : ID of the character we want to check status
        
        Returns:
            bool: the flip status of the input character
        """
        return self.character_dict[character_id].flipped

    def print_board_state(self):
        """
        prints the current state of the game board in the console 
        """
        columns = 3
        column_width = 15
        print("\nCurrent board state:")
        for i, name in enumerate(self.character_dict, 1):
            
            if self.character_dict[name].flipped:
                name = (f"x{name}x")
            
            print(f'{name:<{column_width}}', end='')

            if i % columns == 0:
                print()

        if len(self.character_dict) % columns != 0:
            print()
