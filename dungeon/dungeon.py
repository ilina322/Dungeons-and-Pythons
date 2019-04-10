class Dungeon:
    def __init__(self):
        self._map = self.create_map()

    def create_map(self):
        f = open('level.txt', 'r')
        map_str = f.read()
        map_lst = map_str.split('\n')
        return map_lst


    def print_map(self):
        for row in self._map:
            print(row)

d = Dungeon()
d.print_map()

