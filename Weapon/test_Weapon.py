import unittest
from Weapon import *


class TestDungeonsAndPythonsClassWeapon(unittest.TestCase):
    def test_initial_value(self):
        w = Weapon(name="The Axe of Destiny", damage=20)
        assert w.name == "The Axe of Destiny"
        assert w.damage == 20

    def test_str_method(self):
        w = Weapon(name="The Axe of Destiny", damage=20)
        expected_result = ""'name: The Axe of Destiny \ndamage: 20'""
        self.assertEqual(str(w), expected_result)

    def test_repr_method(self):
        w = Weapon(name="The Axe of Destiny", damage=20)
        expected_result = ""'name: The Axe of Destiny \ndamage: 20'""
        self.assertEqual(repr(w), expected_result)



if __name__ == '__main__':
    unittest.main()
