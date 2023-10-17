from game_classes import Character, Weapon
import random, sys, time

# This fucntion creates an instance of the character and sword. 
def create_player():
    sword = Weapon(10, 20, 1, 0)
    name = delayed_input("\nPlease enter you characters name: ")
    created_player = Character(name, 50, "Human", sword)
    return created_player

# This function will create an instance of a goblin that is the same level as the player. 
def create_goblin():
    sword = Weapon(10, 20, 1, 0)
    created_goblin = Character("Goblin", 50, "Goblin", sword) 
    return created_goblin

# This function is called if block is False and will output different statements for the player or the opponent. 
def output_if_not_block(_attacker, _opponent, _tactic, _damage):
    if _attacker.race == "Human":
        delayed_print(f"\nYour {_tactic} Attack was successful, you have reduced the {_opponent.name}'s Health by {_damage} points.") 
    else:
        delayed_print(f"\nYour block was unsuccessful. The {_attacker.name} reduced your Health by {_damage} points.")

# This function is called if block is True and will output different statements for the player or the opponent.
def output_if_block(_attacker, _opponent, _tactic):
    if _attacker.race == "Human":
        delayed_print(f"\nThe {_opponent.name} blocked your {_tactic} Attack.")
    elif _opponent.race == "Human":
        delayed_print(f"\nYou successfully blocked the {_attacker.name}'s {_tactic} Attack.")

# This fucntion will use a int as a key for a dictionary and retrun the associated word. 
def convert_int_to_word(player_choice):
    attacks = {1: "Light", 2: "Heavy", 3: "Block", 4: "Parry"}
    return attacks.get(int(player_choice), 3)

def character_combat(_attacker, _opponent, _attack_tactic):
    # If the opponents block is False, then reduce opponents health by the calculated damage of the attack (Light or Heavy). 
    if not _opponent.block(_attacker, _attack_tactic):
        damage_points = _attacker.attack(_opponent, _attack_tactic)
        _attacker.weapon.add_xp(damage_points /2)
        output_if_not_block(_attacker, _opponent, _attack_tactic, damage_points)
    
    # Otherwise no damage is dealt to the opponent and the attackers turn is over. 
    else:
       output_if_block(_attacker, _opponent, _attack_tactic)

# This function is used to parry against an attack. 
def parry(_defender, _opponent, defender_tactic):
    if not _opponent.block(_defender, defender_tactic):
        damage_to_enemy = _defender.parry(_opponent)
        # Add weapon xp for successful hit 
        _defender.weapon.add_xp(damage_to_enemy /2)
        delayed_print(f"\nYour {defender_tactic} was succsessful, and you delt {damage_to_enemy} points of damage to the {_opponent.name}")
    else:
        damage_to_player = _opponent.parry(_defender)
        delayed_print(f"\nYour {defender_tactic} was unsuccessful and the {_opponent.name} reduced your health by {damage_to_player} points.")

# This fucntion will return the NPC's randomly selected attack choice, in the form of a string "Light" or "Heavy" attack.
def enemy_random_attack():
    num = random.randint(1,2)
    word = convert_int_to_word(num)
    return word

# This function will delay text that is outputed to the terminal. 
def delayed_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    # Add a newline character at the end of the text
    sys.stdout.write('\n')
    sys.stdout.flush()

# This function will delay test that is output to the terminal and retrun the inputed value. 
def delayed_input(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()




    

 

   



   




