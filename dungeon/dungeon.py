import random
import json
import sys
sys.path.insert(0, '../hero')
sys.path.insert(0, '../enemy')
sys.path.insert(0, '../fight')
sys.path.insert(0, '../person')
from hero import *
from enemy import *
from fight import *
from person import *

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

    def equip_enemy(self, enemy):
        random_equip_enemy = random.randint(1,3)
        if random_equip_enemy == 1:
            spell = self.generate_random_spell()
            enemy.learn(spell)
        elif random_equip_enemy == 2:
            weapon = self.generate_random_weapon()
            enemy.equip(weapon)
        elif random_equip_enemy == 3:
            spell = self.generate_random_spell()
            weapon = self.generate_random_weapon()
            enemy.equip(weapon)
            enemy.learn(spell)


    def battle(self, enemy):
       self.equip_enemy(enemy)
       fight = Fight(self.hero, enemy)
       fight.start()
       hero_wins = fight.hero_wins()
       return hero_wins

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
                self.in_fight = True

                enemy = self.enemies[new_hero_position]
                hero_wins = self.battle(enemy)
                if hero_wins:
                    del self.enemies[new_hero_position] #remove enemy from map
                    self._map[curr_hero_position[0]][curr_hero_position[1]] = '.'
                    self._map[new_hero_position[0]][new_hero_position[1]] = 'H'
                else:
                    self._map[curr_hero_position[0]][curr_hero_position[1]] = '.'
                    self.hero._health = self.hero._max_health
                    self.hero._mana = self.hero._max_mana
                    respawn = self.spawn(self.hero)
                    if respawn == False:
                        print('Game over')

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


def main():
    command = ''
    h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    d = Dungeon('level.txt')
    d.spawn(h)
    d.create_enemies()
    w = Weapon(name='Sword', damage=20)
    s = Spell(name='Fireball', damage=30, mana_cost=20, cast_range=2)
    d.hero.learn(s)
    d.hero.equip(w)
    d.print_map()

    while(True):
        command = input("Enter command: ")
        if command == 'w':
            d.move_hero('up')
        elif command == 'a':
            d.move_hero('left')
        elif command == 's':
            d.move_hero('down')
        elif command == 'd':
            d.move_hero('right')
        elif command == 'c':
            d.hero_attack(by='spell')
        d.print_map()

    e = Enemy(health=100, mana=150, damage=10)
    d.start_battle(e)

if __name__ == '__main__':
    main()



