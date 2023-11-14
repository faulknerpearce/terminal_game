from game_functions import convert_int_to_word, character_combat, enemy_random_attack, parry, delayed_print, delayed_input


def arena(_player, _opponent):

    delayed_print(
        f"\nWelcome to the Arena {_player.name}.\nYou are facing a level {_opponent.level} {_opponent.race}.")

    while _player.health > 0 and _opponent.health > 0:

        if _player.health > 0 and _opponent.health > 0:

            # Players attacking choice.
            choice = delayed_input(f"\nIt is your turn to attack the {_opponent.name}\nPress 1 to perform a Light Attack or Press 2 to perform a Heavy Attack: ")

            # Ensure that the input is only the number 1 or 2.
            while choice != "1" and choice != "2":
                delayed_print("\nIncorrect input for your attack, Try again.")
                choice = delayed_input(
                    "Press 1 to perform a Light Attack or 2 to perform a Heavy Attack: ")

            player_attack_tactic = convert_int_to_word(int(choice))

            # Player's attacking trun.
            character_combat(_player, _opponent, player_attack_tactic)
        else:
            break

        if _player.health > 0 and _opponent.health > 0:

            choice = delayed_input(
                f"\nThe {_opponent.name} is about to attack you! \nPress 3 to attempt to block the attack, Press 4 to attempt a parry: ", 0.03)

            # Ensure that the input is only the number 3 or 4.
            while choice != "3" and choice != "4":
                delayed_print(
                    "\nIncorect input for your defence, try again.", 0.03)
                choice = delayed_input(
                    "Press 3 to block, Press 4 to parry: ", 0.03)

            # Get the NPC's randomly selected attack.
            enemy_attacking_tactic = enemy_random_attack()

            player_defence_tactic = convert_int_to_word(int(choice))

            # Player's defending turn.
            if player_defence_tactic == "Block":
                character_combat(_opponent, _player, enemy_attacking_tactic)

            else:
                parry(_player, _opponent, player_defence_tactic)

        else:
            break

        delayed_print(f"\nYou have {_player.health} health points remaining,")
        delayed_print(
            f"and the {_opponent.name} has {_opponent.health} health points remaining.")


def main_world(_player):
    pass
