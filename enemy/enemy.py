import sys
sys.path.insert(0, '../person')
sys.path.insert(0, '../weapon')
from person import *
class Enemy(Person):
    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self._damage = damage

    def __str__(self):
        return 'health: {0}\nmana: {1}\ndamage:{2}'.format(self._health, self._mana, self._damage)

    @property
    def damage(self):
        return self._damage

    def attack(self, by=None):
        if by == 'weapon':
            if self._weapon != None:
                return self._weapon.damage
        elif by == 'spell':
            if self._spell != None:
                self._mana -= self._spell.mana_cost
                return self._spell.damage
        return self._damage
