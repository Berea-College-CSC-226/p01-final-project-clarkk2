class Player:
    def __init__(self, name):
        self.name = name
        self.fashion_score = 0
        self.health = 100
        self.clothes = {
            "shirt": None,
            "pants": None,
            "shoes": None,
            "hat": None
        }
        self.special_ability = None

    def move(self, direction):
        pass

    def apply_ability(self, ability_name):
        pass

    def customize(self, clothes):
        pass

    def check_collision(self, obstacle):
        pass

    def collect_item(self, item):
        pass