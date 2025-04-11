"""This class represents a character storing name, file location and flip status"""

class Character:
    """
    Represents a character on the game board, keeping track of its flip status.

    Attributes:
        name (str): The name of the character.
        flipped (bool): The current flip status of character, initialized to False.
    """
    def __init__(self, name, image_path):
        """
        Initializes a new character instance.

        Args:
            name (str): The name to assign to the character.
        """
        self.flipped = False
        self.name = name
        self._image_path = image_path

    def flip(self):
        """
        marks the character as flipped
        """
        self.flipped = True

    def get_image_path(self):
        """
        Returns the image file path
        """
        return self._image_path

    def __str__(self):
        """
        Returns a string representation of the player.

        Returns:
            str: A string showing the player's name and score.
        """
        return self.name
