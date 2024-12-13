import pygame

class Platform:
    def __init__(self, x, y, width, height, image_path=None, crop_rect=None):
        """
        Initialize the platform.
        :param x: X-coordinate of the platform.
        :param y: Y-coordinate of the platform.
        :param width: Width of the platform.
        :param height: Height of the platform.
        :param image_path: Path to the platform image (optional).
        :param crop_rect: Tuple (x, y, w, h) to crop the image (optional).
        """
        self.rect = pygame.Rect(x, y, width, height)

        if image_path:
            try:
                # Load the image
                self.image = pygame.image.load(image_path).convert_alpha()

                if crop_rect:
                    # Crop the image to the specified area
                    self.image = self.image.subsurface(crop_rect)

                # Scale the cropped image to the platform dimensions
                self.image = pygame.transform.scale(self.image, (width, height))

            except Exception as e:
                print(f"Failed to load or crop platform image: {e}")
                self.image = None
        else:
            self.image = None  # No image provided

        # Default colors for fallback
        self.color = (139, 69, 19)  # Brown for wooden platforms
        self.highlight_color = (160, 82, 45)  # Slightly lighter brown

    def draw(self, screen):
        """
        Draw the platform on the screen.
        :param screen: The Pygame screen surface.
        """
        if self.image:
            # Draw the scaled platform image
            screen.blit(self.image, self.rect.topleft)
        else:
            # Draw a fallback rectangle
            pygame.draw.rect(screen, self.highlight_color, self.rect)
            pygame.draw.line(screen, self.color, self.rect.topleft, self.rect.bottomright, 3)
            pygame.draw.line(screen, self.color, self.rect.bottomleft, self.rect.topright, 3)