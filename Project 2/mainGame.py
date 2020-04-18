# Author- Bedabrata Bora
# Project 2- A very Simple terminal game

from classes.game import Character, Colors
from classes.magic import Spell


# Create black magic
fire = Spell(name="Fire", cost=20, dmg=150, type="Black")
thunder = Spell(name="Thunder", cost=10, dmg=80, type="Black")
quake = Spell(name="Quake", cost=15, dmg=100, type="Black")
hurricane = Spell(name="Hurricane", cost=25, dmg=180, type="Black")
hydro = Spell(name="Hydro Pump", cost=30, dmg=200, type="Black")

# Create White Magic
cure = Spell(name="Cure", cost=12, dmg=120, type="White")
heal = Spell(name="Heal", cost=20, dmg=200, type="White")

powers = [fire, thunder, quake, hurricane, hydro, cure, heal]

player = Character(hp=460, mp=80, atk=80, df=40, magic=powers)      # Player stats
enemy = Character(hp=1200, mp=65, atk=60, df=30, magic=[])      # Enemy stats

game = True     # Game is running

while game:
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    player.select_action()
    choice = input("Select an option: ")
    index = int(choice)-1

    if index == 0:                              # Player wishes to attack
        player_attack_dmg = player.generate_dmg()
        enemy.take_dmg(player_attack_dmg)
        print("You did ", player_attack_dmg, " damage.", "Enemy HP: ", enemy.get_hp())
    elif index == 1:                            # Player wishes to cast magic
        player.select_magic()
        magic_choice = int(input("Choose a magic: ")) - 1
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_spell_dmg()

        current_mp = player.get_mp()

        # Check if enough MP is available to caste spell
        if spell.cost > current_mp:
            print(Colors.FAIL + "Not enough MP" + Colors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        enemy.take_dmg(magic_dmg)
        print(Colors.OKBLUE + spell.name + " deals ", str(magic_dmg), "damage", Colors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.generate_dmg()
    player.take_dmg(enemy_dmg)
    print(Colors.FAIL, "Enemy did ", enemy_dmg, " damage.", "Player HP: ", player.get_hp(), Colors.ENDC)

    print("---------------------------------------------------")
    print("Enemy HP: ", Colors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Colors.ENDC)
    print("Your HP: ", Colors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Colors.ENDC)
    print("Your MP: ", Colors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + Colors.ENDC)

    if player.get_hp() == 0:
        print(Colors.FAIL + Colors.BOLD + "YOU LOSE!" + Colors.ENDC)
        game = False
    elif enemy.get_hp() == 0:
        print(Colors.FAIL + Colors.BOLD + "YOU WIN!" + Colors.ENDC)
        game = False

