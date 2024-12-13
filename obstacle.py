import pygame

class Coin:
    def __init__(self, x, y, radius=10, color=(255, 215, 0)):
        """
        Represents a coin collectible.
        :param x: X-coordinate of the coin.
        :param y: Y-coordinate of the coin.
        :param radius: Radius of the coin (default is 10 for circular coins).
        :param color: Color of the coin (default is gold).
        """
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.radius = radius
        self.color = color

    def draw(self, screen):
        """Draw the coin as a circle."""
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

    def collect(self, player):
        """
        Check if the coin is collected by the player.
        :param player: The player object.
        :return: True if the player collects the coin, False otherwise.
        """
        return self.rect.colliderect(player.rect)