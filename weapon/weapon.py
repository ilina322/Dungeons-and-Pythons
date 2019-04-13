
class Weapon:

    def __init__(self, name, damage):
        self._name = name
        self._damage = damage

    def __str__(self):
        return 'name: {} \ndamage: {}'.format(self._name, self._damage)

    def __repr__(self):
        return str(self)

    @property
    def damage(self):
        return self._damage

    @property
    def name(self):
        return self._name

def main():
    pass

if __name__ == '__main__':
    main()