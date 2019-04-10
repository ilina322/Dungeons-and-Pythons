import sys
sys.path.insert(0, '../spell')
from spell import *
class Person:
    def __init__(self, health, mana, mana_regeneration_rate):
        self._mana_regeneration_rate = mana_regeneration_rate
        self._max_health = health
        self._max_mana = mana
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
            if self._health > self._max_health:
                self._health = self._max_health
        return True

    def take_mana(self):
        self._mana += self._mana_regeneration_rate
        if self._mana > self._max_mana:
            self._mana = self._max_mana

    def attack():
        pass

    def take_damage(self, damage):
        self._health -= damage
