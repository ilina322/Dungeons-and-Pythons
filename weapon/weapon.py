
class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return 'name: {} \ndamage: {}'.format(self.name, self.damage)

    def __repr__(self):
        return str(self)

def main():
    pass

if __name__ == '__main__':
    main()