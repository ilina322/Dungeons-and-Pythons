import unittest
import sys
sys.path.insert(0, '../')
from enemy import *
from weapon import *
class TestEnemy(unittest.TestCase):


    def test_init_values(self):
        e = Enemy(health=20, mana=10, damage=10)
        self.assertEqual(e.health, 20)
        self.assertEqual(e.mana, 10)
        self.assertEqual(e.damage, 10)

    def test_attack_if_weapon_is_available_then_return_weapon_damage(self):
        e = Enemy(health=20, mana=10, damage=10)
        w = Weapon()


if __name__ == '__main__':
    unittest.main()