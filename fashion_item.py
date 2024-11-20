class FashionItem:
    def __init__(self, item_type, name, points):
        self.item_type = item_type  # e.g., "shirt", "pants", "shoes"
        self.name = name
        self.points = points

    def apply_to_player(self, player):
        pass

    def display_info(self):
        pass