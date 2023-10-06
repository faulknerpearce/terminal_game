from game_functions import create_player, create_goblin, convert_int_to_word, character_combat, enemy_random_attack, parry
def level_one(_player, _goblin):

    print(f"\nWelcome to the Arena\nYou are facing a level {_goblin.level} {_goblin.race}.")

    while _player.health > 0 and _goblin.health > 0:

        if _player.health > 0 and _goblin.health > 0:

            # Players attacking choice. 
            choice = input(f"\nIt is your turn to attack the {_goblin.name}\nPress 1 to perform a Light Attack or Press 2 to perform a Heavy Attack: ")
    
            # Ensure that the input is only either the number 1 or 2. 
            while choice != "1" and choice!= "2":
                print("\nIncorrect input for your attack, Try again.")
                choice = input("Press 1 to perform a Light Attack or 2 to perform a Heavy Attack: ")
    
            player_attack_tactic = convert_int_to_word(int(choice))
    
            # Player's attacking trun.   
            character_combat(_player, _goblin, player_attack_tactic)
        else:
            break

        if _player.health > 0 and _goblin.health > 0:

            choice = input(f"\nThe {_goblin.name} is about to attack you! \nPress 3 to attempt to block the attack, Press 4 to attempt a parry: ")
    
            # Ensure that the input is only either the number 3 or 4. 

            while choice != "3" and choice != "4":
                print("\nIncorect input for your defence, try again.")
                choice = input("Press 3 to block, Press 4 to parry: ")
 
            # Get the NPC's randomly selected attack. 
            enemy_attacking_tactic = enemy_random_attack()

            player_defence_tactic = convert_int_to_word(int(choice))
    
            # Player's defending turn. 
            if player_defence_tactic == "Block":
                character_combat(_goblin, _player, enemy_attacking_tactic)
        
            else:
                parry(_player, _goblin, player_defence_tactic)
                
        else:
            break

        print(f"\nYou have {_player.health} health points remaining,")
        print(f"and the {_goblin.name} has {_goblin.health} health points remaining.")
