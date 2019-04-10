class Spell:

    def __init__(self,name=None, damage=0, mana_cost=0, cast_range=0):
        self._name = name
        self._damage = damage
        self._mana_cost = mana_cost
        self._cast_range = cast_range

    def __str__(self):
        return 'spell: {0}\ndamage: {1}\nmana cost:{2}\ncast range: {3}'.format(self.name, self.damage, self.mana_cost, self.cast_range)

    @property    
    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    @property
    def damage(self):
        return self._damage

    def set_damage(self, damage):
        self._damage = damage

    @property
    def mana_cost(self):
        return self._mana_cost

    def set_mana_cost(self, mana_cost):
        self._mana_cost = mana_cost

    @property
    def cast_range(self):
        return self._cast_range

    def set_cast_range(self, cast_range):
        self._cast_range = cast_range
