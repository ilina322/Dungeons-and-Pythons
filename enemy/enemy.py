import sys
sys.path.insert(0, '../person')
from person import *
class Enemy(Person):
    def __init__(self, health=20, mana=10, damage=10):
        super().__init__(health, mana)
        self._damage = damage

    def __str__(self):
        return 'health: {0}\nmana: {1}\ndamage:{2}'.format(self._health, self._mana, self._damage)

    @property
    def damage(self):
        return self._damage

    def attack(self, by):
        if by == 'weapon':
            if self._weapon != None:
                return self._weapon.damage
        else:
            if self._spell != None:
                return self._spell.damage
        return self._damage

    
e = Enemy(health=20, mana=20, damage=20)
print(str(e))