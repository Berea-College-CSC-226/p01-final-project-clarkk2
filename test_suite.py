import unittest
from player import Player
from npc import NPC
from fashion_item import FashionItem
from sound_manager import SoundManager
from game_manager import GameManager
from obstacle import Obstacle
from item import Item

class TestPlayer(unittest.TestCase):
    def test_initial_fashion_score(self):
        player = Player("TestPlayer")
        self.assertEqual(player.fashion_score, 0)

# Add more tests for other classes here

if __name__ == '__main__':
    unittest.main()