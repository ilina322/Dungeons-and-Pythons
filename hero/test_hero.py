import unittest
from hero import *

class TestDungeonsAndPythonsClassHero(unittest.TestCase):
    def test_initial_value(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        assert h._name == "Bron"
        assert h._title == "Dragonslayer"
        assert h._mana_regeneration_rate == 2


    def test_method_known_as_which_returns_string_with_name_and_title_of_the_hero(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        expected_result = "Bron the Dragonslayer"
        self.assertEqual(h.known_as(), expected_result)

    def test_method_attack_when_weapon_is_passed_and_hero_is_not_equip_then_returns_zero(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertEqual(h.attack('weapon'), 0)

    def test_method_attack_when_weapon_is_passed_and_hero_is_equip_then_returns_weapons_damage(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        w = Weapon('my_weapon', 20)
        h.equip(w)
        self.assertEqual(h.attack('weapon'), 20)

    def test_method_attack_when_spell_is_passed_and_hero_have_not_learn_any_spell_then_returns_zero(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertEqual(h.attack('spell'), 0)

    def test_method_attack_when_weapon_is_passed_and_hero_know_spell_returns_spell_damage(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        s = Spell('aha', 30, 4, 3)
        h.learn(s)
        self.assertEqual(h.attack('spell'), 30)



if __name__ == '__main__':
    unittest.main()
