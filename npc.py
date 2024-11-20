class NPC:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0)
        self.speed = 1
        self.difficulty = 1

    def chase_player(self, player):
        pass

    def steal_points(self, player):
        pass

    def adjust_difficulty(self):
        pass