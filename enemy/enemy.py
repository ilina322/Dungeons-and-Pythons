import sys
sys.path.insert(0, '../person')
from person import *
class Enemy(Person):
    def __init__(self, health=20, mana=10, damage=10):
        super().__init__(health, mana)
        self._damage = damage

    def __str__(self):
        return 'health: {0}\nmana: {1}\ndamage:{2}'.format(self._health, self._mana, self._damage)
        

e = Enemy(health=20, mana=20, damage=20)
print(str(e))