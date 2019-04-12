import unittest
import dungeon
from dungeon import *

class TestClassDungeon(unittest.TestCase):
    def test_initial_value(self):
        d = Dungeon('level.txt')
        assert d.file_name == 'level.txt'

    def test_create_map_when_file_attribute_is_empty_then_retutns_empty_list(self):
        d = Dungeon('empty.txt')
        self.assertEqual(d.create_map(), [])

    def test_create_map_when_file_attribute_is_not_empty_then_loads_map_from_it_and_returns_list_of_rows(self):
        d = Dungeon('level.txt')
        expected_result = [['.', '.', '#', '#', '.', '.', 'S', '.', '.', 'T'], ['#', 'T', '#', '#', 'S', '.', '#', '#', '#', '.'], ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'], ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'], ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']]
        self.assertEqual(d.create_map(), expected_result)

    def test_spawn_when_there_is_no_S_location_on_the_map_then_return_false(self):
        d = Dungeon('empty.txt')
        d._map = [['.', '.', '#', '#', '.', '.', '#', '.', '.', 'T'], ['#', 'T', '#', '#', '#', '.', '#', '#', '#', '.'], ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'], ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'], ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']]
        self.assertEqual(d.spawn(), False)

    def test_spawn_when_there_are_S_locations_on_the_map_then_spawn_hero_in_first_S_location_and_return_true(self):
        d = Dungeon('level.txt')
        assert d.spawn() == True
        expected_result = [['.', '.', '#', '#', '.', '.', 'H', '.', '.', 'T'], ['#', 'T', '#', '#', 'S', '.', '#', '#', '#', '.'], ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'], ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'], ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']]
        self.assertEqual(d._map, expected_result)

    def test_can_move_when_is_passed_coordinat_that_is_out_of_range_then_return_false(self):
        d = Dungeon('level.txt')
        self.assertEqual(d.can_move(-1, 7), False)

    def test_can_move_when_you_try_to_move_into_an_obstacle_then_return_false(self):
        d = Dungeon('level.txt')
        self.assertEqual(d.can_move(0, 3), False)


    def test_can_move_when_you_try_to_move_into_an_enemy_then_return_message_that_a_figth_is_started(self):
        d = Dungeon('level.txt')
        self.assertEqual(d.can_move(2, 9), 'Start a fight!')

    def test_can_move_when_you_try_to_move_into_treasure_then_return_message_that_a_treasure_is_found(self):
        d = Dungeon('level.txt')
        self.assertEqual(d.can_move(1, 1), 'Found treasure!')

    def test_find_hero_position_that_returns_tuple_with_current_hero_position(self):
        d = Dungeon('level.txt')
        d.spawn()
        self.assertEqual(d.find_hero_position(), (0, 6))

    def test_move_hero_when_is_passed_direction_that_will_move_him_into_a_obstacle_then_return_false(self):
        d = Dungeon('level.txt')
        d.spawn()
        self.assertEqual(d.move_hero('down'), False)


    def test_move_hero_when_is_passed_direction_that_will_move_him_into_an_enemy_then_return_message_that_a_figth_is_started(self):
        d = Dungeon('level.txt')
        d.spawn()
        d.move_hero('left')
        d.move_hero('down')
        self.assertEqual(d.move_hero('down'), 'Start a fight!')

    def test_hero_move_when_is_passed_direction_that_will_move_him_into_treasure_then_return_message_that_a_treasure_is_found(self):
        d = Dungeon('level.txt')
        d.spawn()
        d.move_hero('right')
        d.move_hero('right')
        self.assertEqual(d.move_hero('right'), 'Found treasure!')

    def test_move_hero_when_is_passed_direction_that_will_move_him_outside_the_map_then_return_false(self):
        d = Dungeon('level.txt')
        d.spawn()
        self.assertEqual(d.move_hero('up'), False)

    def test_when_generate_random_spell_then_return_spell_instance(self):
        d = Dungeon('level.txt')
        s = d.generate_random_spell()
        self.assertTrue(isinstance(s, Spell)) 

    def test_when_generate_random_weapon_then_return_weapon_instance(self):
        d = Dungeon('level.txt')
        w = d.generate_random_weapon()
        self.assertTrue(isinstance(w, Weapon)) 




if __name__ == '__main__':
    unittest.main()
