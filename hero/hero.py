import sys
sys.path.insert(0, '../person')
sys.path.insert(0, '../spell')
sys.path.insert(0, '../weapon')

from person import *
from spell import *
from weapon import *


class Hero(Person):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana, mana_regeneration_rate)
        self._name = name
        self._title = title

    def known_as(self):
        return "{hero_name} the {hero_title}".format(hero_name = self._name, hero_title = self._title)


    def attack(self, by):
        if by == 'weapon':
            if self._weapon != None:
                return self._weapon.damage
        else:
            if self._spell != None:
                self._mana -= self._spell.mana_cost
                return self._spell.damage
        return 0

def main():
    pass


if __name__ == "__main__":
    main()