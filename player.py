import pygame

class Player:
    def __init__(self, image_path, x=100, y=400):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.velocity = [0, 0]
        self.on_ground = True

    def update(self, platforms, obstacles):
        # Apply gravity
        self.velocity[1] += 1  # Gravity effect
        if self.velocity[1] > 10:
            self.velocity[1] = 10

        # Move the player
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Collision detection with platforms
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity[1] > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity[1] = 0
                    self.on_ground = True

        # Check obstacle collisions
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                print("Collision with obstacle!")

    def move(self, direction):
        if direction == 'left':
            self.velocity[0] = -5
        elif direction == 'right':
            self.velocity[0] = 5

    def stop(self):
        self.velocity[0] = 0

    def jump(self):
        if self.on_ground:
            self.velocity[1] = -15  # Jump force

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self.rect))