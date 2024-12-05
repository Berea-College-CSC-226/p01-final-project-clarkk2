import pygame
from game_manager import GameManager


def main():
    """
    Main function to run the Fashion Demon game.
    """
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Set game window size
    pygame.display.set_caption("Fashion Demon")
    clock = pygame.time.Clock()

    # Initialize the GameManager
    game_manager = GameManager()
    game_manager.start_game()

    # Load images (update paths with actual image locations)
    player_image = pygame.image.load("images/player.png")
    npc_image = pygame.image.load("images/npc.png")
    obstacle_image = pygame.image.load("images/obstacle.png")
    item_image = pygame.image.load("images/item.png")

    # Fonts for text display
    font = pygame.font.Font(None, 36)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            game_manager.player.move("up")
        if keys[pygame.K_DOWN]:
            game_manager.player.move("down")
        if keys[pygame.K_LEFT]:
            game_manager.player.move("left")
        if keys[pygame.K_RIGHT]:
            game_manager.player.move("right")

        # Update the game state
        game_manager.update()

        # Clear the screen
        screen.fill((0, 0, 0))  # Black background

        # Draw the player
        screen.blit(player_image, (game_manager.player.position[0] * 50, game_manager.player.position[1] * 50))

        # Draw NPCs
        for npc in game_manager.npcs:
            screen.blit(npc_image, (npc.position[0] * 50, npc.position[1] * 50))

        # Draw obstacles
        for obstacle in game_manager.obstacles:
            screen.blit(obstacle_image, (obstacle.position[0] * 50, obstacle.position[1] * 50))

        # Draw items
        for item in game_manager.fashion_items:
            screen.blit(item_image, (item.position[0] * 50, item.position[1] * 50))

        # Display the player's score and health
        score_text = font.render(f"Fashion Score: {game_manager.player.fashion_score}", True, (255, 255, 255))
        health_text = font.render(f"Health: {game_manager.player.health}", True, (255, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(health_text, (10, 50))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    # Quit the game
    print("Exiting the game...")
    pygame.quit()


if __name__ == "__main__":
    main()