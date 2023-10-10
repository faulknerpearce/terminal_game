from game_functions import create_player, create_goblin, delayed_print, delayed_input
from game_data_functions import save_character, get_saved_character
from game_levels import level_one

# Game main menu
delayed_print(f"welcome to the Gladiators game.")
keyboard = delayed_input("Press 1 to start a new game. Press 2 to continue from a saved game. ")

if keyboard == "2":
    choice, characters = get_saved_character()

else: 
    choice = '2'  

# Begining of the new game. 
if choice == '2': 
    delayed_print("\nYou slowly open your eyes, trying to adjust to the darkness. \nYou feel a cold metal chain around your wrist, and as you try to move, you realize you're chained to a wall. \nSuddenly, you hear heavy footsteps approaching. A prison guard bursts into the room, his eyes scanning the cell. \n'On your feet, maggot!' he barks, his voice echoing through the walls.")
    delayed_print("\nYou struggle to stand up, your legs weak from being chained for so long. The guard unlocks your chains and drags you out of the cell. \nYou're pushed into a dimly lit arena, surrounded by cheering crowds. The guard turns to you and asks, 'What is your name?'")

    player = create_player()
    goblin = create_goblin()

    # This is the players first combat level in the game. 
    level_one(player, goblin)
else: 
    pass
    # Load saved character. 
    #player = load_player()

# Print the results of the fight. 
if player.health <= 0:
    delayed_print("\nGame Over! You were defeated by the Goblin.")
else:
    delayed_print("\nCongratulations! You defeated the Goblin.")
    player.weapon.check_xp()
    save_character(player)
    

