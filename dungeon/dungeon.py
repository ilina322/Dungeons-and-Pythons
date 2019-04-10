
import sys
sys.path.insert(0, '../hero')
from hero import *

class Dungeon:
    def __init__(self):
        self._map = self.create_map()

    def create_map(self):
        f = open('level.txt', 'r')
        map_str = f.read()
        map_lst = map_str.split('\n')
        map_list = []
        for row in map_lst:
            list_col = [sympol for sympol in row]
            map_list.append(list_col)
        return map_list


    def print_map(self):
        for row in self._map:
            print(''.join(row))

    def spawn(self):
        hero = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        for row in range(len(self._map)):
            for col in range(len(self._map[0])):
                if self._map[row][col] == 'S':
                    self._map[row][col] = 'H'
                    return True
        return False



d = Dungeon()

d.spawn()
d.print_map()


