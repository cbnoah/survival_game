import json

from game.player import Player


def save_game(player: Player):
    """
    Save the current game state and stores it in a json internal file.
    :param player: the current player
    """
    try:
        with open('./data/saves/saves.json', 'w', encoding='utf-8') as f:
            json.dump({
                "name": player.name,
                "hunger": player.hunger,
                "thirst": player.thirst,
                "energy": player.energy,
            }, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        raise FileNotFoundError('data file not found')

def load_game() -> Player:
    """
    Load the current game state and stores it in a json internal file.é
    :return player: the info taken from the file
    """
    try:
        with open('./data/saves/saves.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError('data file not found')
    return Player(data['name'], data['hunger'], data['thirst'], data['energy'])

def is_there_info() -> bool:
    try:
        with open('./data/saves/saves.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            if data['name'] == '':
                return False
            return True
    except FileNotFoundError:
        raise FileNotFoundError('data file not found')