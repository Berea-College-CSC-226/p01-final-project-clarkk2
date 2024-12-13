import pygame

class Player:
    def __init__(self, image_path, x, y, scale=(50, 100)):
        # Load and scale the player image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.jump_strength = 15
        self.gravity = 1
        self.on_ground = False
        self.score = 0  # Track the player's score

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def jump(self):
        self.velocity.y = -self.jump_strength
        self.on_ground = False

    def apply_gravity(self):
        self.velocity.y += self.gravity
        self.rect.y += self.velocity.y

    def check_platform_collisions(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity.y > 0:
                self.rect.bottom = platform.rect.top
                self.velocity.y = 0
                self.on_ground = True

    def update(self, platforms):
        self.handle_input()
        self.apply_gravity()
        self.check_platform_collisions(platforms)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def collect_coin(self, coin):
        """Handles collecting a coin."""
        if self.rect.colliderect(coin.rect):
            self.score += 1  # Increase the player's score
            return True  # Indicate the coin should be removed
        return False