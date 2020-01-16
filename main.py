from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)
                
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
        spell = int(input("Choose magic:")) - 1
        magic_dmg = player.generate_spell_damage(spell)
        spellname = player.get_spellname(spell)
        spellcost = player.get_spellcost(spell)

        current_mp = player.get_mp()
        if spellcost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spellcost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spellname + " deals", str(magic_dmg) + bcolors.ENDC)


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



