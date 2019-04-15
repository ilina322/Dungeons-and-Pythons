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
        self.map = self.create_map()
        self.hero = None
        self.in_fight = False
        self.hero_is_on_start_position = False
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
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] == 'E':
                    new_enemy = Enemy(health = random.randint(1,10)*10, mana = random.randint(1,15)*10, damage = random.randint(1,20))
                    self.enemies.update({(row, col) : new_enemy})

    def print_map(self):
        for row in self.map:
            print(''.join(row))

    def spawn(self, hero):
        self.hero = hero
        self.hero._health = self.hero.max_health
        self.hero._smana = self.hero.max_mana
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] == 'H':
                    self.map[row][col] = '.'
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] == 'S':
                    self.map[row][col] = 'H'
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
            self.hero.take_mana(mana_points)
            print(str(mana_points) + " mana!")
        elif treasure == 2:
            health_points = random.randint(1,30)
            self.hero.take_healing(health_points)
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
        for k, v in self.enemies.items():
                    if v == enemy:
                        row, col = k
                        if hero_wins:
                            self.map[row][col] = '.'
                            del self.enemies[k]
                            break
        if not fight.hero_wins():
            respawn = self.spawn(self.hero)
            if respawn == False:
                print('Game over')
                return True

    def can_move(self, row, col):
        if col >= len(self.map[0]) or col < 0 or row >= len(self.map) or row < 0 or self.map[row][col] == '#':
            return False
        return True

    def find_hero_position(self):
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] == 'H':
                    return (row, col)

    def find_new_position(self, direction):
        curr_hero_position = self.find_hero_position()
        if direction == 'up':
            can_move_on = self.can_move(curr_hero_position[0] - 1, curr_hero_position[1])
            new_hero_position = (curr_hero_position[0] - 1, curr_hero_position[1])

        elif direction == 'down':
            can_move_on = self.can_move(curr_hero_position[0] + 1, curr_hero_position[1])
            new_hero_position = (curr_hero_position[0] + 1, curr_hero_position[1])

        elif direction == 'left':
            can_move_on = self.can_move(curr_hero_position[0], curr_hero_position[1] - 1)
            new_hero_position = (curr_hero_position[0], curr_hero_position[1] - 1)

        else:
            can_move_on = self.can_move(curr_hero_position[0], curr_hero_position[1] + 1)
            new_hero_position = (curr_hero_position[0], curr_hero_position[1] + 1)
        if can_move_on:
            return new_hero_position
        else: 
            return None

    def move_hero(self, direction):
        curr_hero_position = self.find_hero_position()
        new_hero_position = self.find_new_position(direction)
        if new_hero_position != None:
            if self.map[new_hero_position[0]][new_hero_position[1]] == "T":
                print('Found treasure!')
                self.win_random_treasure()
                self.save_spawn_point(curr_hero_position)
                self.map[new_hero_position[0]][new_hero_position[1]] = 'H'
            elif self.map[new_hero_position[0]][new_hero_position[1]] == "E":
                self.in_fight = True
                enemy = self.enemies[new_hero_position]
                self.battle(enemy)

            elif self.map[new_hero_position[0]][new_hero_position[1]] == "S":
                self.save_spawn_point(curr_hero_position)
                self.hero_is_on_start_position = True
                self.map[new_hero_position[0]][new_hero_position[1]] = 'H'

            elif self.map[new_hero_position[0]][new_hero_position[1]] == "G":
                self.save_spawn_point(curr_hero_position)
                print('You win')
            else:
                self.save_spawn_point(curr_hero_position)
                self.map[new_hero_position[0]][new_hero_position[1]] = 'H'

    def check_for_enemy_in_range(self, spell_range):
        curr_hero_position = self.find_hero_position()
        row, col = curr_hero_position
        for num in range(1, spell_range + 1):
            if row + num < len(self.map) and row - num >= 0 and col + num < len(self.map[0]) and col - num >= 0:
                if self.map[row + num][col] == 'E':
                    return self.enemies[(row + num, col)]
                elif self.map[row][col + num] == 'E':
                    return self.enemies[(row, col + num)]
                elif self.map[row - num][col] == 'E':
                    return self.enemies[(row - num, col)]
                elif self.map[row][col - num] == 'E':
                    return self.enemies[(row, col - num)]
        return None

    def save_spawn_point(self, curr_hero_position):
        if self.hero_is_on_start_position:
            self.map[curr_hero_position[0]][curr_hero_position[1]] = 'S'
            self.hero_is_on_start_position = False
        else:
            self.map[curr_hero_position[0]][curr_hero_position[1]] = '.'

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
              if self.check_for_enemy_in_range(self.hero._spell.cast_range) != None:
                e = self.check_for_enemy_in_range(self.hero._spell.cast_range)
                self.battle(e)

                print("There are enemies near you!")
                return True
              else:
                print('Nothing in casting range {0}, or not enough space to cast {1}'.format(self.hero._spell.cast_range, self.hero._spell.name))
            else:
                print('you do not know any spell')


def main():
    command = ''
    h = Hero(name="Bron", title="Dragonslayer", health=10, mana=100, mana_regeneration_rate=2)
    d = Dungeon('cast_test_map.txt')
    d.spawn(h)
    d.create_enemies()
    w = Weapon(name='Sword', damage=20)
    s = Spell(name='Fireball', damage=0, mana_cost=20, cast_range=2)
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

if __name__ == '__main__':
    main()



