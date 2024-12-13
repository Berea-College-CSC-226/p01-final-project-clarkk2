import pygame
from player import Player
from npc import NPC
from platform import Platform
from obstacle import Coin

class GameManager:
    def __init__(self, screen_width, screen_height):
        # Initialize game dimensions
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Load background
        try:
            self.background = pygame.image.load("GameImage/background.png").convert()
        except Exception as e:
            print(f"Failed to load background image: {e}")
            self.background = None

        # Player and NPC
        self.player = Player("GameImage/tacocat.png", 100, 500)
        self.npc = NPC("GameImage/fashiondemon.png", self.player.rect.x - 200, 500)  # Spawn NPC farther back

        # Platforms
        self.platforms = [
            Platform(100, 500, 300, 40, "GameImage/platform_image.png", (50, 50, 1445, 1950)),
            Platform(450, 400, 250, 30, "GameImage/platform_image1.png", (60, 60, 1000, 1940)),
            Platform(700, 300, 200, 20, "GameImage/platform_image1.png"),
        ]

        # Coins
        self.coins = [
            Coin(150, 450),
            Coin(300, 350),
            Coin(600, 250),
        ]

        # Score Font
        self.font = pygame.font.Font(None, 36)  # Default font, size 36

    def update(self):
        # Update player
        self.player.update(self.platforms)

        # Check if player falls off the map
        if self.player.rect.y > self.screen_height:
            print("Player fell off the map!")
            self.game_over(pygame.display.get_surface())

        # Update NPC to chase the player
        self.npc.update(self.player)

        # Check for coin collection
        for coin in self.coins[:]:
            if coin.collect(self.player):
                self.coins.remove(coin)  # Remove collected coin
                self.player.score += 1  # Update score

        # Check for NPC collision with the player
        if self.npc.check_collision(self.player):
            self.player_caught_effect()
            self.game_over(pygame.display.get_surface())  # Show Game Over screen

        # Check for level completion
        self.check_level_completion()

    def draw(self, screen):
        # Draw background
        if self.background:
            screen.blit(self.background, (0, 0))
        else:
            screen.fill((135, 206, 250))  # Default to light blue if background fails

        # Draw platforms
        for platform in self.platforms:
            platform.draw(screen)

        # Draw coins
        for coin in self.coins:
            coin.draw(screen)

        # Draw player and NPC
        self.player.draw(screen)
        self.npc.draw(screen)

        # Draw score in the top-left corner
        score_text = self.font.render(f"Score: {self.player.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def game_over(self, screen):
        """Display a Game Over screen."""
        screen.fill((0, 0, 0))  # Black background
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, (255, 0, 0))  # Red bold text
        screen.blit(text, (self.screen_width // 2 - text.get_width() // 2, self.screen_height // 2 - text.get_height() // 2))

        # Display final score
        score_text = self.font.render(f"Final Score: {self.player.score}", True, (255, 255, 255))
        screen.blit(score_text, (self.screen_width // 2 - score_text.get_width() // 2, self.screen_height // 2 + 50))

        pygame.display.flip()

        # Wait for player to restart or quit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Press 'R' to restart
                        waiting = False
                        self.reset_game()  # Reset the game state

    def reset_game(self):
        """Reset the game to its initial state."""
        self.__init__(self.screen_width, self.screen_height)  # Reinitialize the GameManager

    def check_level_completion(self):
        """Check if the player has reached the end of the level."""
        if self.player.rect.x >= self.screen_width - 50:  # Adjust threshold as needed
            self.level_complete()

    def level_complete(self):
        """Handle level completion."""
        print("Level Complete!")
        self.display_message("Congratulations!")
        self.next_level()

    def display_message(self, message):
        """Show a temporary message on screen."""
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))  # Black background
        font = pygame.font.Font(None, 72)
        text = font.render(message, True, (0, 255, 0))  # Green text
        screen.blit(text, (self.screen_width // 2 - text.get_width() // 2, self.screen_height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(3000)

    def next_level(self):
        """Transition to the next level with increased difficulty."""
        self.__init__(self.screen_width, self.screen_height)  # Reset game manager
        self.npc.speed += 1  # Increase NPC speed for difficulty

    def player_caught_effect(self):
        """Play a caught animation or effect."""
        for _ in range(5):
            self.player.image.set_alpha(128)  # Make player semi-transparent
            pygame.display.flip()
            pygame.time.delay(100)
            self.player.image.set_alpha(255)  # Reset alpha
            pygame.display.flip()