"""Testing Character Class"""
import unittest
import src.model.character as character

class TestCharacter(unittest.TestCase):
    """Testing Character Class"""
    def setUp(self):
        """Set up method to create a Character instance before each test."""
        self.character1 = character.Character("Mario", "/path/to/mario.png")
        self.character2 = character.Character("Luigi", "/path/to/luigi.png")

    def test_character_creation(self):
        """Test if a Character instance is created correctly."""
        self.assertEqual(self.character1.name, "Mario")
        self.assertEqual(self.character1.image_path, "/path/to/mario.png")
        self.assertFalse(self.character1.flipped)

        self.assertEqual(self.character2.name, "Luigi")
        self.assertEqual(self.character2.image_path, "/path/to/luigi.png")
        self.assertFalse(self.character2.flipped)

    def test_flip_method_single_character(self):
        """Test the flip method to ensure it sets the flipped status to True."""
        self.assertFalse(self.character1.flipped)
        self.character1.flip()
        self.assertTrue(self.character1.flipped)

    def test_flip_method_multiple_characters(self):
        """Test the flip method to ensure it sets the flipped status to True."""
        self.assertFalse(self.character1.flipped)
        self.character1.flip()
        self.assertTrue(self.character1.flipped)

        self.assertFalse(self.character2.flipped)
        self.character2.flip()
        self.assertTrue(self.character2.flipped)

    def test_flip_method_back(self):
        """Test that flip method return to original state when run twice"""
        self.assertFalse(self.character1.flipped)
        self.character1.flip()
        self.assertTrue(self.character1.flipped)
        self.character1.flip()
        self.assertFalse(self.character1.flipped)

    def test_string_representation(self):
        """Test the __str__ method for the correct string representation."""
        self.assertEqual(str(self.character1), "Mario")
        self.assertEqual(str(self.character2), "Luigi")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
