import json

from game.player import Player


def save_game(player: Player, day_survived: int) -> None:
    """
    Save the current game state and stores it in a json internal file.
    :param day_survived: the number of days survived
    :param player: the current player
    """
    try:
        with open('./data/saves/saves.json', 'w', encoding='utf-8') as f:
            json.dump({
                "name": player.name,
                "hunger": player.hunger,
                "thirst": player.thirst,
                "energy": player.energy,
                "days_survived": day_survived
            }, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        raise FileNotFoundError('data file not found')

def load_game() -> dict:
    """
    Load the current game state and stores it in a json internal file.é
    :return player: the info taken from the file
    """
    try:
        with open('./data/saves/saves.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError('data file not found')
    return {"player":Player(data['name'], data['hunger'], data['thirst'], data['energy']), "days_survived": data['days_survived'] if data['days_survived'] < 60 else 0}

def is_there_info() -> bool:
    try:
        with open('./data/saves/saves.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            if data == {} or data is None:
                return False
            return True
    except FileNotFoundError:
        raise FileNotFoundError('data file not found')