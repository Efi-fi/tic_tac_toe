import json
from cmd_game.rendering import clr

default_player = 'Unknown'
default_filename = './game_info/settings.json'

modes = {'1': 'Comp VS Player',
         '2': 'Player 1 VS Player 2'}

default_setting = {
    'Player 1': default_player,
    'Player 2': default_player,
    'Level': 'Random',  # [AI, Random, Hard, Low]
    'Who first': 'Random',  # [Random, Player, Comp] for mode 2, 3 always Random
    'Statistic filename': './game_info/statistics.json',
}

sm = {'main': ['Play', 'Settings', 'Statistics', 'Exit'],
      'play': ['One player', 'Two players', 'Back'],
      'settings': list(default_setting) + ['Back'],
      'level': ['Low', 'Random', 'Hard', 'AI', 'Back'],
      'who first': ['Comp', 'Player', 'Random', 'Back'],
      }


def read_setting(filename=default_filename):
    """
    Read setting from file.
    """
    settings = default_setting
    try:
        with open(filename) as json_file:
            settings = json.load(json_file)
    except:
        save_settings(settings)
    finally:
        return settings


def save_settings(settings, filename=default_filename):
    """
    Save settings into JSON file.
    """
    with open(filename, 'w') as json_file:
        json.dump(settings, json_file, indent=4)


def input_set(settings, menu, selected_point):
    """
    Changing settings from menu.
    """
    point_name = menu[-1][selected_point]
    if point_name in settings and point_name != 'Statistic filename':
        clr()
        value = input(f'Please input value for {point_name}: ')
        if value:
            settings[point_name] = value
        else:
            input_set(settings, menu, selected_point)  # use recursion while not correct input
    elif len(menu) > 1:
        if point_name in sm['level'] and menu[-1][0] == 'Low':
            settings['Level'] = point_name
        elif point_name in sm['who first']:
            settings['Who first'] = point_name
