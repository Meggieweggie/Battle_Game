

wizard = "Wizard"
elf = "Elf"
human = "Human"
wizard_hp =70
elf_hp =100
human_hp =150
wizard_damage =150
elf_damage =100
human_damage =20
dragon_hp = 300
dragon_damage = 50
character=""
my_hp=0
my_damage=0
battle_continues=1
character_selection =0
while character_selection ==0:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    character_selection = input("Choose your character: ")

    if character_selection == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        character_selection = 1
    elif character_selection == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        character_chosen = 1
    elif character_selection == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        character_selection = 1
    else:
        print("Unknown character")
        character_selection=0

battle_continues =1
while battle_continues == 1:
    dragon_hp -= my_damage
    print("The {} damaged the Dragon!".format(character))
    if dragon_hp <=0:
        print("The dragon has lost the battle!")
        battle_continues =0
    else:
        my_hp -= dragon_damage
        print("The Dragon damaged the {}!".format(character))
        if my_hp <=0:
            print("The {} has lost the battle!".format(character))
            battle_continues=0

