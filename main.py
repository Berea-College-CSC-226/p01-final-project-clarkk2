from game_manager import GameManager


def main():
    """
    Main function to run the Fashion Demon game.
    """
    # Initialize the GameManager
    game_manager = GameManager()

    # Start the game
    game_manager.start_game()

    # Display welcome message and controls
    print("\nWelcome to Fashion Demon!")
    print("Can you escape the Fashion Demon and collect legendary items?")
    print("\nControls:")
    print("- Type 'pause' to pause the game.")
    print("- Type 'resume' to resume the game.")
    print("- Type 'quit' to exit the game.")
    print("- Type 'status' to view the current game state.\n")

    # Game loop
    while game_manager.game_state == "running":
        try:
            # Update game state
            game_manager.update()

            # Prompt user for input
            user_input = input("Enter a command (pause/resume/quit/status): ").lower()

            # Handle input
            if user_input == "pause":
                print("\nGame paused. Type 'resume' to continue.")
                game_manager.game_state = "paused"
                while game_manager.game_state == "paused":
                    resume_input = input("> ").lower()
                    if resume_input == "resume":
                        game_manager.game_state = "running"
                        print("\nGame resumed.")
            elif user_input == "quit":
                print("\nExiting the game...")
                game_manager.end_game()
                break
            elif user_input == "status":
                print(f"\nCurrent Game State:\n{game_manager}\n")
            else:
                print("Invalid command. Try 'pause', 'resume', 'quit', or 'status'.\n")

        except KeyboardInterrupt:
            # Handle interruptions (Ctrl+C)
            print("\nGame interrupted. Exiting...")
            game_manager.end_game()
            break

    # End game cleanup
    print("Thank you for playing Fashion Demon! See you next time.")


if __name__ == "__main__":
    main()
