import unittest
from person import *
import sys
sys.path.insert(0, '../spell')
sys.path.insert(0, '../weapon')
from spell import *
from weapon import *

class TestPerson(unittest.TestCase):

    def test_init_values(self):
        p = Person(health=20, mana=10, mana_regeneration_rate=10)
        self.assertEqual(p.health, 20)
        self.assertEqual(p.mana, 10)

    def test_when_take_damage_then_subtract_given_damage_from_person_health(self):
        p = Person(health=100, mana=100, mana_regeneration_rate=10)
        p.take_damage(30)
        self.assertEqual(p.health, 70)

    def test_when_heal_then_return_true_if_is_alive_and_add_healing_points_to_health(self):
        p = Person(health=100, mana=100, mana_regeneration_rate=10)
        p.take_damage(50)
        p.take_healing(20)
        self.assertEqual(p.health, 70)

    def test_when_heal_then_return_false_if_is_dead(self):
        p = Person(health=100, mana=100, mana_regeneration_rate=10)
        p.take_damage(110)
        self.assertFalse(p.take_healing(20))

    def test_is_alive_when_person_health_is_not_positive_then_return_false(self):
        p = Person(health = 50, mana=100, mana_regeneration_rate=10)
        p.take_damage(60)
        expected_result = False
        self.assertEqual(p.is_alive(), expected_result)

    def test_can_cast_when_person_mana_is_not_enough_for_spell_then_return_false(self):
        p = Person(health = 50, mana=10, mana_regeneration_rate=10)
        s = Spell(name='Fireball', damage=10, mana_cost=20, cast_range=1)
        self.assertFalse(p.can_cast(s))

    def test_when_take_mana_then_add_mana_points_to_mana(self):
        p = Person(health=100, mana=100, mana_regeneration_rate=10)
        p._mana -= 30
        p.take_mana()
        self.assertEqual(p.mana, 80)

    def test_when_equip_person_then_set_person_weapon_to_given_one(self):
        p = Person(health=100, mana=100, mana_regeneration_rate=10)
        w = Weapon( 'hammer', 20)
        p.equip(w)
        self.assertEqual(p._weapon, w)


    def test_learn_method_that_sets_person_spell_to_given_one(self):
        p = Person(health=100, mana=100, mana_regeneration_rate=10)
        s = Spell('aha', 30, 4, 3)
        p.learn(s)
        self.assertEqual(p._spell, s)

if __name__ == '__main__':
    unittest.main()