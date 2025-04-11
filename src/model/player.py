"""This class represents a player, keeping track of there name and score"""

class Player:
    """
    Represents a player in a game, tracking their name and score.

    Attributes:
        name (str): The name of the player.
        score (int): The current score of the player, initialized to 0.
    """
    def __init__(self, name):
        """
        Initializes a new Player instance.

        Args:
            name (str): The name to assign to the player.
        """
        self.name = name
        self._score = 0

    def add_score(self, points):
        """
        Adds the given number of points to the player's score.

        Args:
            points (int): The number of points to add.
        """
        if points > 0:
            self._score += points
        else:
            raise ValueError("cannot add negative points")
    def reset_score(self):
        """
        Resets score to 0
        """
        self._score = 0

    def get_score(self):
        """
        Returns the current score of the player.

        Returns:
            int: The player's current score.
        """
        return self._score

    def __str__(self):
        """
        Returns a string representation of the player.

        Returns:
            str: A string showing the player's name and score.
        """
        return f"Player: {self.name}, Score: {self._score}"
