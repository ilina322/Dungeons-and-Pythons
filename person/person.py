import sys
sys.path.insert(0, '../spell')
sys.path.insert(0, '../weapon')
from spell import *
from weapon import *

class Person:

    def __init__(self, health, mana, mana_regeneration_rate = 0):

        self._mana_regeneration_rate = mana_regeneration_rate
        self._max_health = health
        self._max_mana = mana
        self._health = health
        self._mana = mana
        self._weapon = None
        self._spell = None

    def is_alive(self):
        return self._health > 0

    def can_cast(self, spell):
        return self._mana > spell.mana_cost

    @property
    def mana_regeneration_rate(self):
        return self._mana_regeneration_rate
    

    @property
    def max_health(self):
        return self._max_health
    
    @property
    def max_mana(self):
        return self._max_mana
    

    @property
    def health(self):
        return self._health

    @property
    def mana(self):
        return self._mana

    @property
    def weapon(self):
        return self._weapon

    @property
    def spell(self):
        return self._spell

    def take_healing(self, healing):
        if not self.is_alive():
            return False
        else:
            self._health += healing
            if self._health > self._max_health:
                self._health = self._max_health
        return True

    def take_mana(self, mana_points=0):
        if self._mana < self._max_mana:
            if mana_points == 0:
                self._mana += self._mana_regeneration_rate
            else:
                self._mana += mana_points

    def take_damage(self, damage):
        self._health -= damage


    def equip(self, weapon):
        self._weapon = weapon

    def learn(self, spell):
        self._spell = spell
