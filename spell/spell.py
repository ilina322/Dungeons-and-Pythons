class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self._name = name
        self._damage = damage
        self._mana_cost = mana_cost
        self._cast_range = cast_range

    def __str__(self):
        return 'spell: {0}\ndamage: {1}\nmana cost:{2}\ncast range: {3}'.format(self.name, self.damage, self.mana_cost, self.cast_range)

    @property    
    def name(self):
        return self._name

    @property
    def damage(self):
        return self._damage

    @property
    def mana_cost(self):
        return self._mana_cost

    @property
    def cast_range(self):
        return self._cast_range
