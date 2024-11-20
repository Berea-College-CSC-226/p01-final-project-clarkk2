import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def test_initial_fashion_score(self):
        player = Player("TestPlayer")
        self.assertEqual(player.fashion_score, 0)

if __name__ == '__main__':
    unittest.main()