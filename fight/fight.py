import sys
sys.path.insert(0, '../hero')
sys.path.insert(0, '../enemy')
from hero import *
from enemy import *
class Fight:

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def first_move(self):
        damage = 0
        text = 'Hero has neither weapon, nor spell! Enemy health is: '
        if self.hero.spell != None:
            if self.hero.weapon != None:
                if self.hero.weapon.damage > self.hero.spell.damage:
                    text = "Hero hits enemy with " + self.hero.weapon.name + ", enemy health is: "
                    damage = self.hero.weapon.damage
                else:
                    text = "Hero casts " + self.hero.spell.name + ", enemy health is: "
                    damage = self.hero.spell.damage
            else:
                text = "Hero casts " + self.hero.spell.name + ", enemy health is: "
                damage = self.hero.spell.damage
        else:
            if self.hero.weapon != None:
                text = "Hero hits enemy with " + self.hero.weapon.name + ", enemy health is: "
                damage = self.hero.weapon.damage
        self.enemy.take_damage(damage)
        text += str(self.enemy.health)
        print(text)