"""Testing Character Class"""
import unittest
import src.model.character as character
import src.model.game_board as game_board

class TestGameBoard(unittest.TestCase):
    """Testing Character Class"""
    def setUp(self):
        """Set up before each test method."""
        self.char1 = character.Character("Alice", "/path/to/Alice.png")
        self.char2 = character.Character("Bob", "/path/to/Bob.png")
        self.char3 = character.Character("Charlie", "/path/to/Charlie.png")
        self.initial_dict = {
            "Alice": self.char1,
            "Bob": self.char2,
            "Charlie": self.char3,
        }
        self.board = game_board.GameBoard(self.initial_dict)

    def test_initialization(self):
        """Test board initialization."""
        self.assertIsNone(self.board.chosen)
        self.assertEqual(len(self.board.character_dict), 3)
        self.assertEqual(self.board.num_unflipped, 3)
        self.assertIsNot(self.board.character_dict, self.initial_dict)
        self.assertEqual(self.board.character_dict["Alice"].name, "Alice")
        self.assertEqual(self.board.character_dict["Bob"].name, "Bob")
        self.assertEqual(self.board.character_dict["Charlie"].name, "Charlie")

    def test_initialization_empty(self):
        """Test board initialization with an empty dictionary."""
        empty_board = game_board.GameBoard({})
        self.assertIsNone(empty_board.chosen)
        self.assertEqual(len(empty_board.character_dict), 0)
        self.assertEqual(empty_board.num_unflipped, 0)

    def test_chose_round_character(self):
        """Test setting the chosen character for the round."""
        self.assertIsNone(self.board.chosen)
        self.board.chose_round_character(self.char1)
        self.assertTrue(self.board.chosen, self.char1)
        self.board.chose_round_character(None)
        self.assertIsNone(self.board.chosen)

    def test_flip_character_single(self):
        """Test flipping a single character."""
        self.assertFalse(self.board.is_flipped("Alice"))
        self.assertEqual(self.board.num_unflipped, 3)
        self.board.flip_character("Alice")
        self.assertTrue(self.board.is_flipped("Alice"))
        self.assertEqual(self.board.num_unflipped, 2)

        self.board.flip_character("Alice")
        self.assertFalse(self.board.is_flipped("Alice"))
        self.assertEqual(self.board.num_unflipped, 3)

    def test_flip_character_multiple(self):
        """Test flipping multiple characters."""
        self.assertEqual(self.board.num_unflipped, 3)
        self.board.flip_character("Alice")
        self.board.flip_character("Charlie")
        self.assertTrue(self.board.is_flipped("Alice"))
        self.assertFalse(self.board.is_flipped("Bob"))
        self.assertTrue(self.board.is_flipped("Charlie"))
        self.assertEqual(self.board.num_unflipped, 1)

    def test_is_flipped(self):
        """Test the is_flipped method."""
        self.assertFalse(self.board.is_flipped("Alice"))
        self.board.flip_character("Alice")
        self.assertTrue(self.board.is_flipped("Alice"))


    def test_reset_board(self):
        """Test resetting the board state."""
        self.board.chose_round_character(self.char2)
        self.board.flip_character("Alice")
        self.board.flip_character("Bob")

        self.assertIsNotNone(self.board.chosen)
        self.assertTrue(self.board.is_flipped("Alice"))
        self.assertTrue(self.board.is_flipped("Bob"))
        self.assertEqual(self.board.num_unflipped, 1)

        self.board.reset_board()

        self.assertIsNone(self.board.chosen)
        self.assertFalse(self.board.is_flipped("Alice"))
        self.assertFalse(self.board.is_flipped("Bob"))
        self.assertFalse(self.board.is_flipped("Charlie"))
        self.assertEqual(self.board.num_unflipped, 3)
