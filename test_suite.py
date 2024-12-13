import unittest
from player import Player
from npc import NPC
from platform import Platform
from obstacle import Coin

class TestGameComponents(unittest.TestCase):
    def setUp(self):
        # Initialize test objects
        self.player = Player("GameImage/tacocat.png", 100, 500)
        self.npc = NPC("GameImage/fashiondemon.png", 700, 500)
        self.platform = Platform(100, 500, 200, 20, "GameImage/platform_image.png")
        self.coin = Coin(150, 450)

    def test_player_movement(self):
        # Simulate player movement
        initial_x = self.player.rect.x
        self.player.rect.x += self.player.speed
        self.assertNotEqual(self.player.rect.x, initial_x, "Player should move when speed is applied")

    def test_player_jump(self):
        # Simulate player jump
        self.player.on_ground = True
        self.player.jump()
        self.assertEqual(self.player.velocity.y, -self.player.jump_strength, "Player jump strength should be applied")

    def test_platform_collision(self):
        # Test player landing on a platform
        self.player.rect.y = self.platform.rect.top - self.player.rect.height
        self.player.apply_gravity()
        self.player.check_platform_collisions([self.platform])
        self.assertTrue(self.player.on_ground, "Player should be on ground after landing on a platform")

    def test_coin_collection(self):
        # Test coin collection
        collected = self.coin.collect(self.player)
        self.assertFalse(collected, "Coin should not be collected if not intersecting player")
        self.player.rect.topleft = self.coin.rect.topleft
        collected = self.coin.collect(self.player)
        self.assertTrue(collected, "Coin should be collected when intersecting player")

    def test_npc_chasing(self):
        # Test NPC following the player
        initial_npc_x = self.npc.rect.x
        self.player.rect.x += 50  # Simulate player moving
        self.npc.update(self.player)
        self.assertNotEqual(self.npc.rect.x, initial_npc_x, "NPC should move toward the player")

if __name__ == "__main__":
    unittest.main()
