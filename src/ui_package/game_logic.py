"""This class represents the logic managing the game flow, turns, and player interaction."""
import src.model.game_board as board
from src.model.player import Player

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
    def __init__(self, rounds, character_dict, player1 : Player, player2 : Player):
        """
        Initializes the players and coresponding game boards, plus sets the win condition 
        """
        self.rounds = rounds
        self.current_player = 0
        self.players = (player1, player2)
        self.game_boards = (board.GameBoard(character_dict), board.GameBoard(character_dict))

    def get_current_player(self):
        """
        Returns the player whose turn it is.
        """
        return self.players[self.current_player]

    def get_current_board(self):
        """
        Returns the current player's board
        """
        return self.game_boards[self.current_player]

    def get_other_player(self):
        """
        Returns the player whose turn it is not.
        """
        return self.players[not self.current_player]
    
    def get_other_board(self):
        """
        Returns ther other player's board
        """
        return self.game_boards[not self.current_player]

    def make_guess(self, guessed_character_id :str):
        """
        Checks if the guessed character maches the target players secret character.
        """
        if self.get_other_board().chosen.name == guessed_character_id:
            self.get_current_player().add_score()
            return True
        else:
            return False

    def win_check(self):
        """
        Checks if the either player has reached the win condition
        """
        if self.players[self.current_player].get_score() == self.rounds:
            return self.players[self.current_player]
        else:
            return None

    def end_turn(self):
        """
        current player chooses to end turn.
        """
        self.current_player = not self.current_player

    def secret_character_setup(self, p1_character, p2_character):
        """
        Sets the secret charcters for the round
        """
        self.game_boards[0].chosen = p1_character
        self.game_boards[1].chosen = p2_character
