import random


class NPC:
    """
    Represents a Non-Player Character (NPC) in the game.
    """

    def __init__(self, name, position=(0, 0), behavior="hostile", speed=1.0):
        """
        Initializes the NPC with a name, position, behavior, and speed.

        :param name: Name of the NPC.
        :param position: Tuple (x, y) representing the NPC's position.
        :param behavior: Behavior type ("hostile", "neutral", "helpful").
        :param speed: Speed at which the NPC moves.
        """
        self.name = name
        self.position = position
        self.behavior = behavior
        self.speed = speed

    def move(self, target_position=None):
        """
        Moves the NPC based on its behavior.

        :param target_position: Optional tuple (x, y) representing the target position (e.g., player's position).
        """
        if self.behavior == "hostile" and target_position:
            # Move towards the player
            self.position = self._move_towards(target_position)
        elif self.behavior == "neutral":
            # Random wandering
            self.position = self._random_wander()
        elif self.behavior == "helpful" and target_position:
            # Move away from the player
            self.position = self._move_away(target_position)

    def interact(self, player, sound_manager):
        """
        Interacts with the player based on the NPC's behavior.

        :param player: The Player object.
        :param sound_manager: The SoundManager object to play sound effects.
        """
        if self.behavior == "hostile":
            # Steal fashion points from the player
            stolen_points = min(10, player.fashion_score)
            player.fashion_score -= stolen_points
            sound_manager.play_sound_effect("steal_points")
            print(f"{self.name} stole {stolen_points} fashion points from {player.name}!")
        elif self.behavior == "helpful":
            # Grant fashion points to the player
            granted_points = 10
            player.fashion_score += granted_points
            sound_manager.play_sound_effect("boost.mp3")
            print(f"{self.name} gave {granted_points} fashion points to {player.name}.")
        elif self.behavior == "neutral":
            print(f"{self.name} does nothing.")

    def _move_towards(self, target_position):
        """
        Moves the NPC one step closer to the target position.

        :param target_position: Tuple (x, y) representing the target position.
        :return: Updated position of the NPC.
        """
        x, y = self.position
        target_x, target_y = target_position
        dx = target_x - x
        dy = target_y - y
        step_x = self.speed if dx > 0 else -self.speed if dx < 0 else 0
        step_y = self.speed if dy > 0 else -self.speed if dy < 0 else 0
        return x + step_x, y + step_y

    def _move_away(self, target_position):
        """
        Moves the NPC one step away from the target position.

        :param target_position: Tuple (x, y) representing the target position.
        :return: Updated position of the NPC.
        """
        x, y = self.position
        target_x, target_y = target_position
        dx = x - target_x
        dy = y - target_y
        step_x = self.speed if dx > 0 else -self.speed if dx < 0 else 0
        step_y = self.speed if dy > 0 else -self.speed if dy < 0 else 0
        return x + step_x, y + step_y

    def _random_wander(self):
        """
        Moves the NPC randomly within a limited range.

        :return: Updated position of the NPC.
        """
        x, y = self.position
        return x + random.choice([-1, 0, 1]) * self.speed, y + random.choice([-1, 0, 1]) * self.speed

    def __str__(self):
        """String representation of the NPC."""
        return f"NPC: {self.name}, Position: {self.position}, Behavior: {self.behavior}, Speed: {self.speed}"
