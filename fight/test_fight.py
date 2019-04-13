import unittest
from fight import *
sys.path.insert(0, '../hero')
sys.path.insert(0, '../enemy')
sys.path.insert(0, '../spell')
sys.path.insert(0, '../weapon')
from hero import *
from enemy import *
from spell import *
from weapon import *

class TestFight(unittest.TestCase):
    
    def test_when_a_fight_is_started_hero_has_no_weapon_and_no_spell_then_dont_hurt_enemy(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        e = Enemy(health=100, mana=100, damage=10, mana_regeneration_rate=2)
        f = Fight(h, e)
        f.first_move()
        self.assertEqual(e.health, 100)

    def test_when_a_fight_is_started_hero_has_only_weapon_then_take_enemy_damage_by_weapon(self):
        w = Weapon(name='Sword', damage=20)
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        e = Enemy(health=100, mana=100, damage=10, mana_regeneration_rate=2)
        h.equip(w)
        f = Fight(h, e)
        f.first_move()
        self.assertEqual(e.health, 80)

    def test_when_a_fight_is_started_hero_has_only_spell_then_take_enemy_damage_by_spell(self):
        s = Spell(name='Fireball', damage=30, mana_cost=20, cast_range=2)
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        e = Enemy(health=100, mana=100, damage=10, mana_regeneration_rate=2)
        h.learn(s)
        f = Fight(h, e)
        f.first_move()
        self.assertEqual(e.health, 70)

    def test_when_a_fight_is_started_hero_has_weapon_stronger_than_spell_then_take_enemy_damage_by_weapon(self):
        w = Weapon(name='Sword', damage=40)
        s = Spell(name='Fireball', damage=30, mana_cost=20, cast_range=2)
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        e = Enemy(health=100, mana=100, damage=10, mana_regeneration_rate=2)
        h.learn(s)
        h.equip(w)
        f = Fight(h, e)
        f.first_move()
        self.assertEqual(e.health, 60)

    def test_when_a_fight_is_started_hero_has_weapon_equal_to_spell_then_take_enemy_damage_by_spell(self):
        w = Weapon(name='Sword', damage=30)
        s = Spell(name='Fireball', damage=30, mana_cost=20, cast_range=2)
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        e = Enemy(health=100, mana=100, damage=10, mana_regeneration_rate=2)
        h.learn(s)
        h.equip(w)
        f = Fight(h, e)
        f.first_move()
        self.assertEqual(e.health, 70)

    def test_when_a_fight_is_started_hero_has_spell_stronger_than_weapon_then_take_enemy_damage_by_spell(self):
        w = Weapon(name='Sword', damage=20)
        s = Spell(name='Fireball', damage=30, mana_cost=20, cast_range=2)
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        e = Enemy(health=100, mana=100, damage=10, mana_regeneration_rate=2)
        h.learn(s)
        h.equip(w)
        f = Fight(h, e)
        f.first_move()
        self.assertEqual(e.health, 70)

if __name__ == '__main__':
    unittest.main()