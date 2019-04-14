import random
import json
import sys
sys.path.insert(0, '../hero')
sys.path.insert(0, '../enemy')
from hero import *
from enemy import *

class Dungeon:
    def __init__(self, file_name):
        self.file_name = file_name
        self._map = self.create_map()
        self.hero = None
        self.in_fight = False
        self.enemies = {}

    def create_map(self):
        with open(self.file_name, 'r') as f:
            map_str = f.read()
        map_lst = map_str.split('\n')
        if len(map_lst) == 1 and len(map_lst[0]) == 0:
            return []

        map_list = []
        for row in map_lst:
            list_col = [sympol for sympol in row]
            map_list.append(list_col)

        return map_list

    def create_enemies(self):
        for row in range(len(self._map)):
            for col in range(len(self._map[0])):
                if self._map[row][col] == 'E':
                    new_enemy = Enemy(health = random.randint(1,10)*10, mana = random.randint(1,15)*10, damage = random.randint(1,15)*10)
                    self.enemies.update({(row, col) : new_enemy})




    def print_map(self):
        for row in self._map:
            print(''.join(row))

    def spawn(self, hero):
        self.hero = hero
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
            if self.hero != None:
                self.hero.equip(weapon)
        elif treasure == 4:
            spell = self.generate_random_spell()
            print(spell.name + " learned!")
            if self.hero != None:
                self.hero.learn(spell)

    def start_battle(self):
        pass

    def can_move(self, row, col):
        if col >= len(self._map[0]) or col < 0 or row >= len(self._map) or row < 0 or self._map[row][col] == '#':
            return False
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
            if self._map[new_hero_position[0]][new_hero_position[1]] == "T":
                print('Found treasure!')
                self.win_random_treasure()
                self._map[curr_hero_position[0]][curr_hero_position[1]] = '.'
                self._map[new_hero_position[0]][new_hero_position[1]] = 'H'
            elif self._map[new_hero_position[0]][new_hero_position[1]] == "E":
                print('Start a fight!')
                self.in_fight = True
                if self.hero_attack(by='weapon') or self.hero_attack(by='spell'):
                    pass
                #return False
            else:
                self._map[curr_hero_position[0]][curr_hero_position[1]] = '.'
                self._map[new_hero_position[0]][new_hero_position[1]] = 'H'

        return can_move_on

    def check_for_enemy_in_range(self, spell_range):
        curr_hero_position = self.find_hero_position()
        row = curr_hero_position[0]
        col = curr_hero_position[1]
        for num in range(1, spell_range + 1):
            if self._map[row + num][col] == 'E':
                return True
            elif self._map[row][col + num] == 'E':
                return True
            elif self._map[row - num][col] == 'E':
                return True
            elif self._map[row][col - num] == 'E':
                return True
        return False


    def hero_attack(self, by):
        curr_hero_position = self.find_hero_position()
        if by == 'weapon':
            if self.hero._weapon != None:
               if self.in_fight:
                   return True
               print('you should be in fight in order to use your weapon')
            else:
                print('you are not equipped')
        else:
            if self.hero._spell != None:
              if self.check_for_enemy_in_range(self.hero._spell.cast_range):
                  return True
              print('Nothing in casting range {}'.format(self.hero._spell.cast_range))
            else:
                print('you do not know any spell')

map = Dungeon('level.txt')
map.create_enemies()
for key, val in map.enemies.items():
    print('{}:{}'.format(key, val))