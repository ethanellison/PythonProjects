from RPG.classes.game import Person, bcolors
from RPG.classes.magic import Spell

# black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 20, 200, "black")
blizzard = Spell("Blizzard", 12, 120, "black")

# white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cure", 18, 200, "white")

player = Person(460, 65, 60, 34, [fire,thunder,blizzard,cure,cura])
enemy = Person(1200, 65, 45, 25, [])
                
running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKED!" + bcolors.ENDC)  # colors the terminal

while running:
    print("===================")
    player.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1
    
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        current_mp = player.get_mp()
        
        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue
        
        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg) + bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for", enemy_dmg)

    print("-------------------------------------")

    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC + "\n")
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC + "\n")
    print("Your magic points:", bcolors.OKBLUE + str(player.get_mp()) + "/"+ str(player.get_max_mp()) +bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "YOU WIN!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You have been defeated" + bcolors.ENDC)
        running = False

    # running = False



