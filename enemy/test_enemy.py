import unittest
from enemy import *
class TestEnemy(unittest.TestCase):

    def test_init_values(self):
        e = Enemy(health=20, mana=10, damage=10)
        self.assertEqual(e.health, 20)
        self.assertEqual(e.mana, 10)
        self.assertEqual(e.damage, 10)
        self.assertEqual(e._max_health, 20)
        self.assertTrue(e.is_alive())

    def test_when_take_damage_then_subtract_given_damage_from_enemy_health(self):
        e = Enemy(health=100, mana=100, damage=20)
        e.take_damage(30)
        self.assertEqual(e.health, 70)

    def test_when_heal_then_return_true_if_is_alive_and_add_healing_points_to_health(self):
        e = Enemy(health=100, mana=100, damage=20)
        e.take_damage(50)
        e.take_healing(20)
        self.assertEqual(e.health, 70)

    def test_when_heal_then_return_false_if_is_dead(self):
        e = Enemy(health=100, mana=100, damage=20)
        e.take_damage(110)
        self.assertFalse(e.take_healing(20))

if __name__ == '__main__':
    unittest.main()