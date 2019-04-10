import random
class Enemy:


    def __init__(self, health=20, mana=10, damage=10):
        self.mana_regeneration_rate = mana_regeneration_rate
        self.max_health = health
        self.health = health
        self.mana = mana
        self.damage = damage


    def __str__(self):
        pass



    def is_alive(self):
        if self._health > 0:
            return True
        else:
            return False

    def can_cast(self):
        if self.mana > 0: #TODO: check current spell mana_cost
            return True
        else:
            return False

    @property
    def health(self):
        return self.health

    @property
    def damage(self):
        return self.damage

    @property
    def mana(self):
        return self.mana

    def take_healing(self, healing):
        if not self.is_alive():
            return False
        else:
            self._health += healing
            if self.health > self.max_health:
                self.health = self.max_health
        return True

    def take_mana(self):
        self.mana += self.mana_regeneration_rate

    def attack():
        pass

    def take_damage(self, damage):
        self.health -= damage
