import sys
sys.path.insert(0, '../spell')
from spell import *
class Person:
    def __init__(self, health=20, mana=10):
        self.max_health = health
        self._health = health
        self._mana = mana

    def is_alive(self):
        return self._health > 0

    def can_cast(self, spell):
        return self._mana > spell.mana_cost

    @property
    def health(self):
        return self._health

    @property
    def mana(self):
        return self._mana

    def take_healing(self, healing):
        if not self.is_alive():
            return False
        else:
            self._health += healing
            if self._health > self.max_health:
                self._health = self.max_health
        return True

    def attack():
        pass

    def take_damage(self, damage):
        self._health -= damage
