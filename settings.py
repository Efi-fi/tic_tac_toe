import json

default_player = 'Unknown'
default_filename = 'settings.json'
default_setting = {
    'Player 1': default_player,
    'Player 2': default_player,
    'Level': 'Random',  # [AI, Random, Hard, Low]
    'Who first': 'Random',  # [Random, Player, Comp] for mode 2, 3 always Random
    'Statistic filename': 'statistics.json',
}


menu = {'main': ['Play', 'Setting', 'Exit'],
        'play': ['One player', 'Two players', 'Back'],
        'settings': list(default_setting) + ['Back'],
        'level': ['Low', 'Medium', 'Hard', 'Back'],
        'who first': ['Comp', 'Player', 'Random', 'Back'],
        }


def read_setting(filename=default_filename):
    settings = default_setting
    try:
        with open(filename) as json_file:
            settings = json.load(json_file)
    except:
        save_settings(settings)
    finally:
        return settings


def save_settings(settings, filename=default_filename):
    with open(filename, 'w') as json_file:
        json.dump(settings, json_file)
