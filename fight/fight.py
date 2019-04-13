import sys
sys.path.insert(0, '../hero')
sys.path.insert(0, '../enemy')
from hero import *
from enemy import *
class Fight:

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def hero_attack(self):
        damage = 0
        text = 'Hero has neither weapon, nor spell! Enemy health is: '
        if self.hero.spell != None:
            if self.hero.weapon != None:
                if self.hero.weapon.damage > self.hero.spell.damage:
                    text = "Hero hits enemy with {}, enemy health is: ".format(self.hero.weapon.name)
                    damage = self.hero.attack(by='weapon')
                else:
                    if self.hero.mana < self.hero.spell.mana_cost:
                         text = 'Hero has not enough mana! Use {}! Enemy health is: '.format(self.hero.weapon.name)
                         damage = self.hero.attack(by='weapon')
                    else:
                        text = "Hero casts {}, enemy health is: ".format(self.hero.spell.name)
                        damage = self.hero.attack(by='spell')
            else:
                if self.hero.mana < self.hero.spell.mana_cost:
                         text = 'Hero has not enough  mana and no weapon! Enemy health is: '
                else:
                    text = "Hero casts {}, enemy health is: ".format(self.hero.spell.name)
                    damage = self.hero.attack(by='spell')
        else:
            if self.hero.weapon != None:
                text = "Hero hits enemy with {}, enemy health is: ".format(self.hero.weapon.name)
                damage = self.hero.attack(by='weapon')
        self.enemy.take_damage(damage)
        text += str(self.enemy.health)
        print(text)

    def enemy_attack(self):
        damage = self.enemy.damage
        text = 'Enemy hits hero for {} damage, hero health is: '.format(damage)
        if self.enemy.spell != None:
            if self.enemy.weapon != None:
                if self.enemy.weapon.damage > self.enemy.spell.damage:
                    text = "Enemy hits hero with {}, hero health is: ".format(self.enemy.weapon.name)
                    damage = self.enemy.attack(by='weapon')
                else:
                    if self.enemy.mana < self.enemy.spell.mana_cost:
                         text = 'Enemy has not enough mana! Enemy uses {}! Enemy health is: '.format(self.enemy.weapon.name)
                         damage = self.enemy.attack(by='weapon')
                    else:
                        text = "Enemy casts {}, hero health is: ".format(self.enemy.spell.name)
                        damage = self.enemy.attack(by='spell')
            else:
                if self.enemy.mana >= self.enemy.spell.mana_cost:
                    text = "Enemy casts {}, hero health is: ".format(self.enemy.spell.name)
                    damage = self.enemy.attack(by='spell')
        else:
            if self.enemy.weapon != None:
                text = "Enemy hits hero with {}, hero health is: ".format(self.enemy.weapon.name)
                damage = self.enemy.attack(by='weapon')
        self.hero.take_damage(damage)
        text += str(self.hero.health)
        print(text)