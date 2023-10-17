from game_classes import Character, Weapon
import json, os

# This will save the players character data (Only to be used for one player it will overwrite all data in the JSON file.) light_damage, _heavy_damage, level, xp
def save_character(player):
    player_stats = {"Name": player.name, "Health": player.health, "Race": player.race, "Level": player.level, "Weapon": {"Light": player.weapon.light_damage, "Heavy": player.weapon.heavy_damage, "Level": player.weapon.level, "XP": player.weapon.xp}}
    with open("player_data.json", "w") as player_data:
        json.dump(player_stats, player_data)

# This will load the player character data from a JSON file. 
def get_saved_character():
    choice = ''
    character = None
    if os.path.isfile("player_data.json"):
        with open("player_data.json", "r") as player_data:
            character = json.load(player_data)
        
        while choice != '1' and choice != '3':
            choice = input(f'Available saved charater: {character["Name"]}, Level {character["Level"]}.\nPress 1 to play a new game, Press 3 to load this character.')
    else:
        choice = '1'
        print('No saved character data found.\nStarting a new game.......')
    return choice, character

# This function will Load a players character and weapon from a dictionary of characters data.
def load_character(data):
    saved_weapon = Weapon(data['Weapon']['Light'], data['Weapon']['Heavy'], data['Weapon']['Level'], data['Weapon']['XP'])
    saved_player = Character(data['Name'], data['Health'], data['Race'], data['Level'], saved_weapon)
    return saved_player