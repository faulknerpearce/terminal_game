# Battle Arena

Battle Arena is a text-based combat game where the player faces off against a goblin in an arena. The player can choose between light and heavy attacks, as well as blocking and parrying enemy attacks. The game continues until either the player or the goblin runs out of health points.

## Features

- Text-based combat system with light and heavy attacks
- Blocking and parrying mechanics for defense
- Weapon leveling system based on experience points
- Character leveling system (not fully implemented in the script)

## Functions and Classes

### Weapon Class

The `Weapon` class represents a weapon with the following attributes:

- `light_damage`: Damage dealt by a light attack
- `heavy_damage`: Damage dealt by a heavy attack
- `level`: The weapon's level, which affects its damage output
- `xp`: Experience points accumulated by the weapon

Methods:

- `level_up()`: Increases the weapon's level
- `check_xp()`: Checks if the weapon has enough experience points to level up
- `add_xp(_xp)`: Adds experience points to the weapon

### Character Class

The `Character` class represents a player or an opponent with the following attributes:

- `name`: The character's name
- `health`: The character's health points
- `weapon`: The character's weapon
- `race`: The character's race (e.g., "Human" or "Goblin")
- `level`: The character's level

Methods:

- `__repr__()`: Returns a string representation of the character
- `attack(_opponent, _attack_tactic)`: Attacks an opponent with a specified tactic (light or heavy)
- `block(_opponent, _attack_key)`: Attempts to block an opponent's attack
- `parry(_enemy)`: Attempts to parry an opponent's attack

### Functions

- `create_player()`: Creates a player character
- `create_goblin()`: Creates a goblin character
- `output_if_not_block(_attacker, _opponent, _tactic, _damage)`: Outputs the result of a successful attack 
- `output_if_block(_attacker, _opponent, _tactic)`: Outputs the result of a successful block
- `convert_int_to_word(player_choice)`: Converts an integer to a corresponding attack or defense tactic
- `character_combat(_attacker, _opponent, _attack_tactic)`: Handles combat between two characters
- `parry(_defender, _opponent, defender_tactic)`: Handles parrying between two characters
- `enemy_random_attack()`: Returns a random attack tactic for the enemy

The main game loop is located at the end of the script, where the player and goblin characters are created, and the combat takes place.