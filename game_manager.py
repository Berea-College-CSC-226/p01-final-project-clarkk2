from player import Player
from npc import NPC
from obstacle import Obstacle
from fashion_item import FashionItem
from sound_manager import SoundManager


class GameManager:
    """
    Manages the overall game flow, including updates, events, and game state.
    """

    def __init__(self):
        """
        Initializes the game manager with default components and state.
        """
        self.player = None
        self.npcs = []
        self.obstacles = []
        self.fashion_items = []
        self.sound_manager = SoundManager()
        self.game_state = "stopped"  # Possible states: "running", "paused", "game_over", "stopped"

    def start_game(self):
        """
        Starts the game by initializing all components and setting the game state to running.
        """
        print("Starting the game...")
        self.player = Player(name="Kamau")
        self.npcs = [
            NPC(name="Fashion Demon", position=(5, 5), behavior="hostile", speed=1.0),
            NPC(name="Style Guru", position=(10, 10), behavior="helpful", speed=1.2)
        ]
        self.obstacles = [
            Obstacle(position=(3, 3), size=(2, 2), damage=10),
            Obstacle(position=(8, 8), size=(1, 1), damage=15)
        ]
        self.fashion_items = [
            FashionItem(position=(4, 4), item_type="hat", style_points=25, rarity="rare"),
            FashionItem(position=(7, 7), item_type="shoes", style_points=50, rarity="legendary")
        ]
        self.sound_manager.play_background_music("background.mp3")
        self.game_state = "running"

    def update(self):
        """
        Updates all game components during a frame.
        """
        if self.game_state != "running":
            return

        # Update NPC movements
        for npc in self.npcs:
            npc.move(target_position=self.player.position)

        # Check for collisions
        self.check_collisions()

    def check_collisions(self):
        """
        Checks for collisions between the player and other objects.
        """
        # Check for player collisions with obstacles
        for obstacle in self.obstacles:
            if obstacle.collide(self.player):
                print(f"Player collided with an obstacle at {obstacle.position}!")

        # Check for player collisions with fashion items
        for item in self.fashion_items[:]:  # Use slicing to avoid modifying the list during iteration
            if item.position == self.player.position:
                item.activate_effect(self.player, self.sound_manager)
                self.fashion_items.remove(item)  # Remove the collected item

        # Check for player collisions with NPCs
        for npc in self.npcs:
            if npc.position == self.player.position:
                npc.interact(self.player, self.sound_manager)

    def end_game(self):
        """
        Ends the game and performs cleanup.
        """
        print("Game Over!")
        self.sound_manager.stop_background_music()
        self.game_state = "game_over"

    def __str__(self):
        """
        Provides a string representation of the current game state.
        """
        return (f"Game State: {self.game_state}, "
                f"Player: {self.player}, "
                f"NPCs: {len(self.npcs)}, "
                f"Obstacles: {len(self.obstacles)}, "
                f"Fashion Items: {len(self.fashion_items)}")
