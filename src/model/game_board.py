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

    def chose_round_character(self, chosen):
        """
        Args:
            chosen (character): The character that the player chooses for the current round
        """

    def reset_board(self):
        """
        resets the game boards by:
            - unflipping all characters
            - reseting the chosen character
        """

    def flip_character(self, character_id):
        """
        flips or unflips a given character

        Args:
            character_id (str) : ID of the character we want to flip
        """

    def is_flipped(self, character_id):
        """
        returns whether or not the charcter is flipped

        Args:
            character_id (str) : ID of the character we want to check status
        """

    def num_unflipped(self):
        """
        returns the number of inflipped characters on the board
        """

    def print_board_state(self):
        """
        prints the current state of the game board in the console 
        """
