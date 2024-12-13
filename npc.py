import pygame

class NPC:
    def __init__(self, image_path, x, y, scale=(50, 100)):
        # Load and scale the NPC image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2  # NPC speed for chasing the player

    def update(self, player):
        # Follow the player horizontally
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        # Follow the player vertically
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def check_collision(self, player):
        """Check if the NPC collides with the player."""
        return self.rect.colliderect(player.rect)