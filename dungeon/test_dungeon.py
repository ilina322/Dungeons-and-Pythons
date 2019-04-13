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
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertEqual(d.spawn(hero), False)

    def test_spawn_when_there_are_S_locations_on_the_map_then_spawn_hero_in_first_S_location_and_return_true(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        assert d.spawn(hero) == True
        expected_result = [['.', '.', '#', '#', '.', '.', 'H', '.', '.', 'T'], ['#', 'T', '#', '#', 'S', '.', '#', '#', '#', '.'], ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'], ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'], ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']]
        self.assertEqual(d._map, expected_result)

    def test_can_move_when_is_passed_coordinat_that_is_out_of_range_then_return_false(self):
        d = Dungeon('level.txt')
        self.assertEqual(d.can_move(-1, 7), False)

    def test_can_move_when_you_try_to_move_into_an_obstacle_then_return_false(self):
        d = Dungeon('level.txt')
        self.assertEqual(d.can_move(0, 3), False)


    def test_can_move_when_you_try_to_move_into_an_enemy_then_true(self):
        d = Dungeon('level.txt')
        self.assertEqual(d.can_move(2, 9), True)

    def test_can_move_when_you_try_to_move_into_treasure_then_return_true(self):
        d = Dungeon('level.txt')
        self.assertEqual(d.can_move(1, 1), True)

    def test_find_hero_position_that_returns_tuple_with_current_hero_position(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        self.assertEqual(d.find_hero_position(), (0, 6))

    def test_move_hero_when_is_passed_direction_that_will_move_him_into_a_obstacle_then_return_false(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        self.assertEqual(d.move_hero('down'), False)


    def test_move_hero_when_is_passed_direction_that_will_move_him_into_an_enemy_then_return_true_and_print_message_that_a_figth_is_started(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        d.move_hero('left')
        d.move_hero('down')
        self.assertEqual(d.move_hero('down'), True)

    def test_hero_move_when_is_passed_direction_that_will_move_him_into_treasure_then_return_true_and_print_message_that_a_treasure_is_found(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        d.move_hero('right')
        d.move_hero('right')
        self.assertEqual(d.move_hero('right'), True)

    def test_move_hero_when_is_passed_direction_that_will_move_him_outside_the_map_then_return_false(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        self.assertEqual(d.move_hero('up'), False)

    def test_when_generate_random_spell_then_return_spell_instance(self):
        d = Dungeon('level.txt')
        s = d.generate_random_spell()
        self.assertTrue(isinstance(s, Spell)) 

    def test_when_generate_random_weapon_then_return_weapon_instance(self):
        d = Dungeon('level.txt')
        w = d.generate_random_weapon()
        self.assertTrue(isinstance(w, Weapon)) 

    def test_check_for_enemy_in_range_when_is_passed_hero_spell_range_and_there_is_no_enemy_in_this_range_then_returns_false(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        spell = Spell(name='Fireball', damage=10, mana_cost=20, cast_range=2)
        d.hero.learn(spell)
        self.assertFalse(d.check_for_enemy_in_range(spell.cast_range))

    def test_check_for_enemy_in_range_when_is_passed_hero_spell_range_and_there_is_enemy_in_this_range_then_returns_true(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        d.move_hero('left')
        spell = Spell(name='Fireball', damage=10, mana_cost=20, cast_range=2)
        d.hero.learn(spell)
        self.assertTrue(d.check_for_enemy_in_range(spell.cast_range))

    def test_hero_attack_when_is_passed_weapon_and_hero_is_not_equipped_with_any_weapon_then_print_message(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        message = 'you are not equipped '
        self.assertEqual(d.hero_attack('weapon'), print(message))

    def test_hero_attack_when_is_passed_weapon_and_hero_is_not_in_fight_then_print_message(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        w = Weapon( 'hammer', 20)
        hero.equip(w)
        message = 'you should be in fight in order to use your weapon'
        self.assertEqual(d.hero_attack('weapon'), print(message))

    def test_hero_attack_when_is_passed_weapon_and_hero_is_in_fight_then_return_true(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        w = Weapon( 'hammer', 20)
        hero.equip(w)
        d.move_hero('left')
        d.move_hero('down')
        d.move_hero('down')
        self.assertTrue(d.hero_attack('weapon'))

    def test_hero_attack_when_is_passed_spell_and_hero_do_not_know_any_spell_then_print_message(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        message = 'you do not know any spell'
        self.assertEqual(d.hero_attack('weapon'), print(message))

    def test_hero_attack_when_is_passed_spell_and_there_is_no_enemy_in_hero_cast_range_then_print_message(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        spell = Spell(name='Fireball', damage=10, mana_cost=20, cast_range=2)
        d.hero.learn(spell)
        message = 'Nothing in casting range {}'.format(d.hero._spell.cast_range)
        self.assertEqual(d.hero_attack('spell'), print(message))

    def test_hero_attack_when_is_passed_spell_and_there_is_enemy_in_hero_cast_range_then_return_true(self):
        d = Dungeon('level.txt')
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d.spawn(hero)
        spell = Spell(name='Fireball', damage=10, mana_cost=20, cast_range=2)
        d.hero.learn(spell)
        d.move_hero('left')
        self.assertTrue(d.hero_attack('spell'))

    def test_when_treasure_is_



if __name__ == '__main__':
    unittest.main()
