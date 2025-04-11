"""Testing Player Class"""
import unittest
import src.model.player as player

class TestPlayer(unittest.TestCase):
    """Testing Player Class"""

    def setUp(self):
        """Set up method to create a Player instance before each test."""
        self.player1 = player.Player("Alice")
        self.player2 = player.Player("Bob")

    def test_player_creation(self):
        """Test if a Player instance is created correctly."""
        self.assertEqual(self.player1.name, "Alice")
        self.assertEqual(self.player1.get_score(), 0)
        self.assertEqual(self.player2.name, "Bob")
        self.assertEqual(self.player2.get_score(), 0)

    def test_add_positive_score(self):
        """Test adding a positive number of points to the score."""
        self.player1.add_score(10)
        self.assertEqual(self.player1.get_score(), 10)
        self.player1.add_score(5)
        self.assertEqual(self.player1.get_score(), 15)

    def test_add_negative_score_raises_value_error(self):
        """Test that adding a negative number of points raises a ValueError."""
        self.player1.add_score(100)
        self.assertEqual(self.player1.get_score(), 100)
        initial_score = self.player1.get_score()
        with self.assertRaises(ValueError) as context:
            self.player1.add_score(-5)
        self.assertEqual(str(context.exception), "cannot add negative points")
        self.assertEqual(self.player1.get_score(), initial_score)

    def test_reset_score(self):
        """Test that resting score sets score to zero"""
        self.player1.add_score(10)
        self.assertEqual(self.player1.get_score(), 10)
        self.player1.reset_score()
        self.assertEqual(self.player1.get_score(), 0)

    def test_get_score(self):
        """Test the get_score method to retrieve the current score."""
        self.assertEqual(self.player1.get_score(), 0)
        self.player1.add_score(25)
        self.assertEqual(self.player1.get_score(), 25)

    def test_string_representation(self):
        """Test the __str__ method for the correct string representation."""
        expected_string1 = "Player: Alice, Score: 0"
        self.assertEqual(str(self.player1), expected_string1)
        self.player1.add_score(30)
        expected_string2 = "Player: Alice, Score: 30"
        self.assertEqual(str(self.player1), expected_string2)
        expected_string3 = "Player: Bob, Score: 0"
        self.assertEqual(str(self.player2), expected_string3)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
