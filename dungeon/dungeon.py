import random
import json
import sys
sys.path.insert(0, '../hero')
from hero import *

class Dungeon:
    def __init__(self, file_name):
        self.file_name = file_name
        self._map = self.create_map()
        self.hero = None

    def create_map(self):
        f = open(self.file_name, 'r')
        map_str = f.read()
        map_lst = map_str.split('\n')
        if len(map_lst) == 1 and len(map_lst[0]) == 0:
            return []

        map_list = []
        for row in map_lst:
            list_col = [sympol for sympol in row]
            map_list.append(list_col)

        f.close()
        return map_list


    def print_map(self):
        for row in self._map:
            print(''.join(row))

    def spawn(self):
        self.hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        for row in range(len(self._map)):
            for col in range(len(self._map[0])):
                if self._map[row][col] == 'S':
                    self._map[row][col] = 'H'
                    return True
        return False

    def generate_random_spell(self):
        with open('treasures.json') as data:
            treasures = json.load(data)
        spells = treasures['spells']
        spell_dict = random.choice(spells)
        return Spell(**spell_dict)

    def generate_random_weapon(self):
        with open('treasures.json') as data:
            treasures = json.load(data)
        weapons = treasures['weapons']
        weapon_dict = random.choice(weapons)
        return Weapon(**weapon_dict)

    def win_random_treasure(self):
        treasure = random.randint(1,4)
        if treasure == 1:
            mana_points = random.randint(1,30)
            print(str(mana_points) + " mana!")
        elif treasure == 2:
            health_points = random.randint(1,30)
            print(str(health_points) + " health!")
        elif treasure == 3:
            weapon = self.generate_random_weapon()
            print(weapon.name + " found!")
            #equip hero with weapon
        elif treasure == 4:
            spell = self.generate_random_spell()
            print(spell.name + " learned!")
            #learn spell

    def can_move(self, row, col):

        if col >= len(self._map[0]) or col < 0 or row >= len(self._map) or row < 0 or self._map[row][col] == '#':
            return False

        elif self._map[row][col] == 'T':
            self.win_random_treasure()
            return 'Found treasure!'

        elif self._map[row][col] == 'E':
            return 'Start a fight!'

        return True

    def find_hero_position(self):
        for row in range(len(self._map)):
            for col in range(len(self._map[0])):
                if self._map[row][col] == 'H':
                    return (row, col)

    def move_hero(self, direction):
        if direction == 'up':
            curr_hero_position = self.find_hero_position()
            can_move_on = self.can_move(curr_hero_position[0] - 1, curr_hero_position[1])
            new_hero_position = (curr_hero_position[0] - 1, curr_hero_position[1])

        elif direction == 'down':
            curr_hero_position = self.find_hero_position()
            can_move_on = self.can_move(curr_hero_position[0] + 1, curr_hero_position[1])
            new_hero_position = (curr_hero_position[0] + 1, curr_hero_position[1])

        elif direction == 'left':
            curr_hero_position = self.find_hero_position()
            can_move_on = self.can_move(curr_hero_position[0], curr_hero_position[1] - 1)
            new_hero_position = (curr_hero_position[0], curr_hero_position[1] - 1)

        else:
            curr_hero_position = self.find_hero_position()
            can_move_on = self.can_move(curr_hero_position[0], curr_hero_position[1] + 1)
            new_hero_position = (curr_hero_position[0], curr_hero_position[1] + 1)

        if can_move_on:
            self._map[curr_hero_position[0]][curr_hero_position[1]] = '.'
            self._map[new_hero_position[0]][new_hero_position[1]] = 'H'

        return can_move_on

    def hero_attack(self, by):
        if by == 'weapon':
            return self.hero._weapon != None
        return self.hero.spell != None








