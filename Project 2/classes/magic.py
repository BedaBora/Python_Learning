import random


class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_spell_dmg(self):
        spell_dmg_low = self.dmg - 15
        spell_dmg_high = self.dmg + 15
        return random.randrange(spell_dmg_low, spell_dmg_high)