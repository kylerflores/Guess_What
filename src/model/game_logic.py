"""This class represents the logic managing the game flow, turns, and player interaction."""

class GameLogic:
    """
    This class sets the standard function of:
        - the game flow
        - player interaction
        - game state
    
    Attributes:
        - rounds (int): first to win x rounds wins
        - player1 (Player): player 1 contains its name and rounds one 
        - player2 (Player): player 2 contains its name and rounds one 
        - player1_board (GameBoard):
        - player2_board (GameBoard):
        
    """
    def __init__(self, rounds, character_dict, player1_name="Player 1", player2_name="Player 2"):
        """
        Initializes the players and coresponding game boards, plus sets the win condition 
        """

    def get_current_player(self):
        """
        Returns the players whose turn it is.
        """

    def get_other_player(self):
        """
        Returns the player whose turn it is not.
        """

    def make_guess(self, guessing_player, guessed_character_id):
        """
        Checks if the guessed character maches the target players secret character.
        """

    def win_check(self):
        """
        Checks if the either player has reached the win condition
        """

    def end_turn(self):
        """
        current player chooses to end turn.
        """
