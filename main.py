from player import Player
from npc import NPC
from fashion_item import FashionItem
from sound_manager import SoundManager
from game_manager import GameManager
from obstacle import Obstacle
from item import Item

def main():
    player = Player("Uriel")  # Set a default player name
    npc = NPC("Leviathan")  # Set NPC name
    sound_manager = SoundManager()
    game_manager = GameManager()

    # Set up the game
    game_manager.player = player
    game_manager.npcs.append(npc)

    # Load background music
    sound_manager.play_background_music()

    # Start the game
    game_manager.start_game()

    # Main game loop
    running = True
    while running:
        # Handle events and update game state
        game_manager.update_game_state()
        print(f"Player: {player.name}, Score: {player.fashion_score}, Health: {player.health}")

        if player.health <= 0:
            print("Game Over!")
            running = False

    game_manager.end_game()

if __name__ == "__main__":
    main()