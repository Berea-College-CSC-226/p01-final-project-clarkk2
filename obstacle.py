class Obstacle:
    def __init__(self, position):
        self.position = position
        self.type = "generic"

    def detect_collision(self, player):
        pass

    def reset_position(self):
        pass
