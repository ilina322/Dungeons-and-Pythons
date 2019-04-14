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
        if self.hero.is_alive():
            damage = 0
            text = 'Hero has neither weapon, nor spell! '
            if self.hero.spell != None:
                if self.hero.weapon != None:
                    if self.hero.weapon.damage > self.hero.spell.damage:
                        text = "{0} hits enemy with {1}! ".format(self.hero.known_as(), self.hero.weapon.name)
                        damage = self.hero.attack(by='weapon')
                    else:
                        if self.hero.mana < self.hero.spell.mana_cost:
                             text = '{0} has not enough mana! Use {1}! '.format(self.hero.known_as(), self.hero.weapon.name)
                             damage = self.hero.attack(by='weapon')
                        else:
                            text = "{0} casts {1}! ".format(self.hero.known_as(), self.hero.spell.name)
                            damage = self.hero.attack(by='spell')
                else:
                    if self.hero.mana < self.hero.spell.mana_cost:
                             text = '{} has not enough mana and no weapon! '.format(self.hero.known_as())
                    else:
                        text = "{0} casts {1}! ".format(self.hero.known_as(), self.hero.spell.name)
                        damage = self.hero.attack(by='spell')
            else:
                if self.hero.weapon != None:
                    text = "{0} hits enemy with {1}! ".format(self.hero.known_as(), self.hero.weapon.name)
                    damage = self.hero.attack(by='weapon')
            self.enemy.take_damage(damage)
            if(self.enemy.is_alive()):
                text += "Enemy health is: {}".format(self.enemy.health)
            else:
                text += "Enemy is dead!"
            print(text)

    def enemy_attack(self):
        if self.enemy.is_alive():
            damage = self.enemy.damage
            text = 'Enemy hits {0} for {1} damage! '.format(self.hero.known_as(), damage)
            if self.enemy.spell != None:
                if self.enemy.weapon != None:
                    if self.enemy.weapon.damage > self.enemy.spell.damage:
                        text = "Enemy hits {0} with {1}! ".format(self.hero.known_as(), self.enemy.weapon.name)
                        damage = self.enemy.attack(by='weapon')
                    else:
                        if self.enemy.mana < self.enemy.spell.mana_cost:
                             text = 'Enemy has not enough mana! Enemy uses {}! '.format(self.enemy.weapon.name)
                             damage = self.enemy.attack(by='weapon')
                        else:
                            text = "Enemy casts {}! ".format(self.enemy.spell.name)
                            damage = self.enemy.attack(by='spell')
                else:
                    if self.enemy.mana >= self.enemy.spell.mana_cost:
                        text = "Enemy casts {}! ".format(self.enemy.spell.name)
                        damage = self.enemy.attack(by='spell')
            else:
                if self.enemy.weapon != None:
                    text = "Enemy hits {0} with {1}! ".format(self.hero.known_as(), self.enemy.weapon.name)
                    damage = self.enemy.attack(by='weapon')
            self.hero.take_damage(damage)
            if(self.hero.is_alive()):
                text += "{0} health is: {1}".format(self.hero.known_as(), self.hero.health)
            else:
                text += "{} is dead!".format(self.hero.known_as())
            print(text)

    def start(self):
        while(self.enemy.is_alive() and self.hero.is_alive()):
            self.hero_attack()
            self.enemy_attack()

    def hero_wins(self):
        if self.enemy.is_alive() and not self.hero.is_alive():
            return False
        elif not self.enemy.is_alive() and self.hero.is_alive():
            return True
        return False


w = Weapon(name='Sword', damage=20)
s = Spell(name='Fireball', damage=30, mana_cost=20, cast_range=2)
h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
e = Enemy(health=100, mana=150, damage=10)
e.learn(s)
h.equip(w)
f = Fight(h, e)
f.start()