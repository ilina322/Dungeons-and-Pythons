import unittest
from hero import *

class TestDungeonsAndPythonsClassHero(unittest.TestCase):
    def test_initial_value(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        assert h.name == "Bron"
        assert h.title == "Dragonslayer"
        assert h.health == 100
        assert h.mana == 100
        assert h.mana_regeneration_rate == 2


    def test_method_known_as_which_returns_string_with_name_and_title_of_the_hero(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        expected_result = "Bron the Dragonslayer"
        self.assertEqual(h.known_as(), expected_result)

    def test_is_alive_when_hero_health_is_not_positive_then_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health = 50, mana=100, mana_regeneration_rate=2)
        h.take_damage(60)
        expected_result = False
        self.assertEqual(h.is_alive(), expected_result)

    


if __name__ == '__main__':
    unittest.main()
