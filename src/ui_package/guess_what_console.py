"""This class represents the logic managing the game flow, turns, and player interaction."""
from src.model.player import Player
import src.model.character as character
from . import game_logic as game_logic

class GuessWhatConsole:
    """
    runs game console mode

    Attributes:
        character_dict (str : character): dictionary of characters
        p1 (Player): Player 1
        p2 (Player): Player 2
    """
    def __init__(self, p1: Player, p2: Player):
        """
        Initializes an instance of the console game.
        """
        self.p1 = p1
        self.p2 = p2
        self.character_dict = {}
        self.game = None

    def init_dict(self):
        """
        Guides the user to set up their characters
        """
        print("Time to set up your board of characters!")
        print("Enter 'done' when you are finished")
        user_input = "input"
        while user_input != "done":
            user_input  = input("Enter the name of a character you would like to add: ")
            if user_input in self.character_dict:
                print("Each character must be unique.")
                continue
            if user_input == "done":
                break
            new_character = character.Character(user_input)
            self.character_dict[user_input] = new_character

    def init_game(self):
        """
        Initiates game logic
        """
        while True:
            try:
                rounds = int(input("\nEnter the number of rounds won needed to win the game: "))
                if rounds > 0:
                    break
                print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")
        print(" ")
        self.game = game_logic.GameLogic(rounds, self.character_dict, self.p1, self.p2)

    def new_round(self):
        """
        Starts a new round and sets up selected secret characters
        """
        p1_pick = "input"
        while p1_pick not in self.character_dict:
            p1_pick = input(f"{self.p1.name} - Enter the name of your secret character: ")
        p1_character = character.Character(p1_pick)
        for i in range(10):
            print(" ")
        p2_pick = "input"
        while p2_pick not in self.character_dict:
            p2_pick = input(f"{self.p2.name} - Enter the name of your secret character: ")
        p2_character = character.Character(p2_pick)
        for i in range(10):
            print(" ")

        self.game.secret_character_setup(p1_character, p2_character)

    def play(self):
        """
        Runs the main console game loop.
        """
        print("\n--- Welcome to Console Guess Who! ---")
        self.init_dict()

        self.init_game()

        round = 1
        print(f"\nRound {round}!")
        
        self.new_round()

        
        while not self.game.win_check():
            print(f"\n\nPlease pass the device to {self.game.get_current_player().name}")
            current_board = self.game.get_current_board()
            user_input = "input"
            while user_input != "guess" and user_input != "end":
                current_board.print_board_state()
                print("\nEnter the name of a character you would like to flip on your board,")
                user_input = input("'guess' to make a guess or 'end' to end your turn: ")
                if user_input == "guess":
                    user_guess = "guess"
                    while user_guess not in current_board.character_dict:
                        user_guess = input("\nEnter the name of the character you would like to guess: ")
                    if self.game.make_guess(user_guess):
                        print(f"\n{self.game.get_current_player().name} guessed correctly!")
                        if self.game.win_check():
                            break
                        round += 1
                        print(f"\nRound {round}!")
                        self.new_round()
                    else:
                        print(f"\n{self.game.get_current_player().name}'s guessed incorrectly!")
                    self.game.end_turn()
                    break
                elif user_input == "end":
                    self.game.end_turn()
                    break
                elif user_input not in current_board.character_dict:
                    print("Please enter a valid character name")
                else:
                    current_board.flip_character(user_input)
        print(f"\n{self.game.win_check().name} wins!")
        print("\nThanks for playing!\n")
