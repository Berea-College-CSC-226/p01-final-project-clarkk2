class Player:
    def __init__(self, name, health=100, fashion_score=0):
        """
        Initialize the player with a name, health, fashion score, and clothing options.

        :param name: The player's name.
        :param health: The player's health (default: 100).
        :param fashion_score: The player's initial fashion score (default: 0).
        """
        self.name = name
        self.health = health
        self.fashion_score = fashion_score
        self.clothes = {
            "shirt": None,
            "pants": None,
            "shoes": None,
            "hat": None
        }
        self.special_ability = None
        self.position = (0, 0)  # Player's initial position

    def move(self, direction):
        """
        Move the player in the given direction.

        :param direction: A tuple (dx, dy) indicating the direction of movement.
        """
        dx, dy = direction
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def apply_ability(self, ability_name):
        """
        Activate the player's special ability.

        :param ability_name: The name of the ability to activate.
        """
        self.special_ability = ability_name
        print(f"{self.name} used special ability: {ability_name}!")

    def customize(self, new_clothes):
        """
        Update the player's clothing options.

        :param new_clothes: A dictionary with clothing items to update.
        """
        for key, value in new_clothes.items():
            if key in self.clothes:
                self.clothes[key] = value
        print(f"{self.name} is now wearing: {self.clothes}")

    def check_collision(self, obstacle):
        """
        Check if the player has collided with an obstacle.

        :param obstacle: An object representing an obstacle.
        :return: True if collision occurs, False otherwise.
        """
        # Assuming obstacle has a position attribute
        if self.position == obstacle.position:
            print(f"{self.name} collided with an obstacle!")
            return True
        return False

    def collect_item(self, item):
        """
        Collect an item and apply its effects.

        :param item: The item to collect.
        """
        if item.type == "fashion":
            self.fashion_score += item.value
        elif item.type == "health":
            self.health = min(self.health + item.value, 100)
        print(f"{self.name} collected a {item.type} item!")

    def __str__(self):
        """String representation of the player."""
        return (f"Player: {self.name}, Health: {self.health}, Fashion Score: {self.fashion_score}, "
                f"Position: {self.position}, Clothes: {self.clothes}")