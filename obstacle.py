class Obstacle:
    """
    Represents an obstacle on the game map.
    """

    def __init__(self, position, size=(1, 1), damage=10):
        """
        Initializes the obstacle with its position, size, and damage value.

        :param position: Tuple (x, y) representing the obstacle's position.
        :param size: Tuple (width, height) representing the obstacle's size.
        :param damage: Integer value representing the damage dealt to the player on collision.
        """
        self.position = position
        self.size = size
        self.damage = damage

    def collide(self, player):
        """
        Checks if the player collides with the obstacle and applies damage if so.

        :param player: The Player object.
        :return: True if a collision occurs, False otherwise.
        """
        px, py = player.position
        ox, oy = self.position
        width, height = self.size

        # Check for collision (basic box overlap detection)
        if ox <= px <= ox + width and oy <= py <= oy + height:
            print(f"Collision detected with obstacle at {self.position}!")
            player.take_damage(self.damage)
            return True
        return False

    def __str__(self):
        """String representation of the obstacle."""
        return f"Obstacle at {self.position} with size {self.size} and damage {self.damage}"
