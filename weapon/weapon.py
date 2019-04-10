
class Weapon:

    def __init__(self, name, damage):
        self.validate_initial_values(name, damage)
        self.name = name
        self.damage = damage

    def validate_initial_values(self, name, damage):

        if not isinstance(name, str):
            raise TypeError('Name of your weapon should be a sting')
        if not isinstance(damage, int):
            raise TypeError('Damage of your weapon should be an integer')
        if damage <= 0:
            raise ValueError('Weapon damage should be positive')

    def __str__(self):
        return 'name: {} \ndamage: {}'.format(self.name, self.damage)

    def __repr__(self):
        return str(self)

def main():
    w = Weapon( ' ', -20)

if __name__ == '__main__':
    main()