from game_classes import Character, Weapon
import json
import os

# This will save the players character data (Only to be used for one player it will overwrite all data in the JSON file.) light_damage, _heavy_damage, level, xp
def save_character(player):
    player_stats = {"Name": player.name, "Health": player.health, "Race": player.race, "Level": player.level, "Weapon": {"Light": player.weapon.light_damage, "Heavy": player.weapon.heavy_damage, "Level": player.weapon.level, "XP": player.weapon.xp}}
    with open("player_data.json", "w") as player_data:
        json.dump(player_stats, player_data)

# This will load the player character data from a JSON file. 
def get_saved_character():
    choice = ''
    character = ''
    if os.path.isfile("player_data.json"):
        with open("player_data.json", "r") as player_data:
            character = json.load(player_data)
        
        while choice != '1' and choice != '2':
            choice = input(f'Available saved charater: {character["Name"]}, Level {character["Level"]}.\nPress 1 to load this character, Press 2 to play a new game.')
    else:
        print('No saved character data.')
    return choice, character

#  This Load a players character and weapon from a dictionary of characters data.
def load_player(data):
    saved_weapon = Weapon(data['Weapon']['Light'], data['Weapon']['Heavy'], data['Weapon']['Level'], data['Weapon']['XP'])
    saved_player = Character(data['Name'], data['Health'], data['Race'], data['Level'], saved_weapon)
    return saved_player

a, b = get_saved_character()







