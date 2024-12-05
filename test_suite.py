from game_manager import GameManager

# Initialize and start the game
game_manager = GameManager()
game_manager.start_game()

# Simulate the game loop
for frame in range(5):  # Simulate 5 frames
    print(f"Frame {frame + 1}")
    game_manager.update()
    print(game_manager)

# End the game
game_manager.end_game()
