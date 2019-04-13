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


    def test_attack_if_weapon_is_available_then_return_weapon_damage(self):
        e = Enemy(health=20, mana=10, damage=10)
        w = Weapon(name='axe', damage=20)
        e.equip(w)
        self.assertEqual(e.attack(by='weapon'), 20)

    def test_attack_if_spell_is_available_then_return_spell_damage(self):
        e = Enemy(health=20, mana=10, damage=10)
        s = Spell(name='magiq', damage=15, mana_cost=10, cast_range=1)
        e.equip(s)
        self.assertEqual(e.attack(by='weapon'), 15)

    def test_attack_if_neither_spell_nor_weapon_is_available_then_return_enemy_damage(self):
        e = Enemy(health=20, mana=10, damage=10)
        self.assertEqual(e.attack(), 10)

if __name__ == '__main__':
    unittest.main()