class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):

        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate


    def known_as(self):
        return "{hero_name} the {hero_title}".format(hero_name = self.name, hero_title = self.title)




def main():
    h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    print(h.is_alive())
    print(h.get_health())
    print(h.get_mana())
    print(h.can_cast())

if __name__ == "__main__":
    main()