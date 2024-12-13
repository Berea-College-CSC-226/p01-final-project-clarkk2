import pygame
from game_manager import GameManager
from sound_manager import SoundManager

# Initialize screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fashion Demon")
    clock = pygame.time.Clock()

    # Game setup
    game_manager = GameManager(SCREEN_WIDTH, SCREEN_HEIGHT)
    sound_manager = SoundManager()
    sound_manager.play_music()  # Corrected method call

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state
        game_manager.update()

        # Draw everything
        screen.fill((135, 206, 250))  # Light blue background
        game_manager.draw(screen)

        # Display update
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
