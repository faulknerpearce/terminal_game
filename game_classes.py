import random
# Class for creating weapons.
class Weapon:
    # Sword attributes.
    def __init__(self, _light_damage, _heavy_damage, level, xp):
        self.level = level
        self.xp = xp
        self.light_damage = _light_damage
        self.heavy_damage = _heavy_damage

    # This method is used to increase the level on the weapon.
    def level_up(self):
        self.level += 1
        self.light_damage += 0.3 * self.level
        self.heavy_damage += 0.5 * self.level

    # This method will increase the weapon level if the current experience is greater than the required experience.
    def check_xp(self):
        required_xp = self.level * 10
        if self.xp > required_xp:
            self.xp -= required_xp
            self.level_up()

    def add_xp(self, _xp):
        self.xp += _xp

# Class for creating the player and opponents.

class Character:
    # Create attributes for the character.
    def __init__(self, _name, _health, _race, _weapon, _level=1):
        self.name = _name
        self.health = _health
        self.race = _race
        self.weapon = _weapon
        self.level = _level

    # This will print information about the Player if they are a human, otherwise it will print the information about the Enemy NPC.
    def __repr__(self):
        if self.race == "Human":
            return f"This characters name is {self.name}, thier level is {self.level} and their current health points are {self.health}."
        else:
            return f"This is a level {self.level} {self.name}."

    # This is a the characters methond for attacking.
    def attack(self, _opponent, _attack_tactic):
        if _attack_tactic == "Light":
            # Light attack damage.
            damage = self.weapon.light_damage
            _opponent.health -= damage
        else:
            # Heavy attack damage.
            damage = self.weapon.heavy_damage
            _opponent.health -= damage
        return damage

    # This method is for the characters defence.
    def block(self, _opponent, _attack_key):
        # adjusted attack rate for light and heavy attack.
        attack_rate = {"Light": 0.6, "Heavy": 0.3, "Parry": 0.4}
        adjusted_rate = attack_rate.get(_attack_key, 1)

        # Calculate the success rate for defense based on skill level difference and attack style.
        success_rate = min(
            1.0, max(0.0, 0.3 + (self.level - _opponent.level) * 0.1 + adjusted_rate))

        # If the random flaot is greater than the success rate this will return True.
        defence = round(random.random(), 1) >= success_rate
        return defence

     # This method will return the result of the players parry attempt.
    def parry(self, _enemy):
        damage_to_enemy = random.randint(
            self.weapon.light_damage, self.weapon.heavy_damage)
        _enemy.health -= damage_to_enemy
        return damage_to_enemy
