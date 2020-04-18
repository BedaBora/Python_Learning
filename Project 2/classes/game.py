import random


# COLOR OPTIONS FOR TERMINAL
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Character:
    # Initialize the characters HP, MP and Damage
    def __init__(self, hp, mp, atk, df, magic):                 # __init__ module acts as a constructor
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_high = atk+20
        self.atk_low = atk-20
        self.df = df
        self.magic = magic
        self.action = ["Attack", "Magic"]

    # Generates a random damage point
    def generate_dmg(self):
        return random.randrange(self.atk_low, self.atk_high)

    # Generates a random magic damage point
    def generate_spell_dmg(self, spell):
        mgc_low = self.magic[spell]["dmg"]-5
        mgc_high = self.magic[spell]["dmg"]+5
        return random.randrange(mgc_low, mgc_high)

    # Reduce the HP by damage taken
    def take_dmg(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    # Get current HP value
    def get_hp(self):
        return self.hp

    # Get max HP of character
    def get_max_hp(self):
        return self.max_hp

    # Get current MP value
    def get_mp(self):
        return self.mp

    # Get max MP of character
    def get_max_mp(self):
        return self.max_mp

    # Reduce MP after casting a spell
    def reduce_mp(self, cost):
        self.mp = self.mp-cost

    # Display list of actions
    def select_action(self):
        index = 1
        print("Actions:")
        for item in self.action:
            print(str(index) + ": ", item)
            index += 1

    # Display list of magic spells
    def select_magic(self):
        index = 1
        print("Magic:")
        for spell in self.magic:
            print(str(index)+":", spell.name, "(cost:", str(spell.cost)+")")
            index += 1

