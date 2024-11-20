class Item:
    def __init__(self, item_type, position):
        self.item_type = item_type  # e.g., "power-up", "fashion item"
        self.position = position

    def activate_effect(self, player):
        pass

    def display_info(self):
        pass