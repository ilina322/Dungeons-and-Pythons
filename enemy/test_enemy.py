import unittest
from enemy import *
class TestEnemy(unittest.TestCase):

    e = Enemy(health=20, mana=10, damage=10)

    def test_init_values(self):
        self.assertEqual(e.health, 20)
        self.assertEqual(e.mana, 10)
        self.assertEqual(e.damage, 10)

if __name__ == '__main__':
    unittest.main()