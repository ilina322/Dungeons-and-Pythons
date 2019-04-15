import unittest
from spell import Spell

class TestSpell(unittest.TestCase):

    def test_init_values(self):
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        assert s.name == 'Fireball'
        assert s.damage == 30
        assert s.mana_cost == 50
        assert s.cast_range == 2

    def test_str_method(self):
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        expected_result = 'spell: Fireball\ndamage: 30\nmana cost:50\ncast range: 2'
        self.assertEqual(str(s), expected_result)


if __name__ == '__main__':
    unittest.main()
