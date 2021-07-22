"""
Statistics:
{
Games:[game1, game2, ... ],
}
"""

import json
import numpy
import platform
import datetime as dt
from cmd_game.tic_tac_toe.settings import default_setting


def read_statistics(filename=default_setting['Statistic filename']):
    """
    Reading statistics from JSON file.
    """
    stats = {}
    try:
        with open(filename) as json_file:
            stats = json.load(json_file)
    except:
        save_statistics(stats)
    finally:
        return stats


def save_statistics(statistics, filename=default_setting['Statistic filename']):
    """
    Saving statistics into JSON file.
    """
    with open(filename, 'w') as json_file:
        json.dump(statistics, json_file, indent=4)


def gen_game_stats(settings: dict, mode: str):
    """
    Creating template statistics for game.
    """
    game_stats = {
        'Game time': dt.datetime.now().isoformat(),
        'Mode': mode,
        'Player 1': settings['Player 1'],
        'Player 2': settings['Player 2'],
        'Comp': platform.uname()[1],
        'Level': settings['Level'],
        'Winner': None,
        'First': None,
        'Moves': 0,
    }
    return game_stats


def show_stat(filename=default_setting['Statistic filename']):
    """
    Generating statistics.
    """
    stats = read_statistics(filename)
    games = stats['Games']
    common_stat = dict()
    common_stat['Games'] = len(games)
    common_stat['Games with comp'] = len([game for game in games if game['Mode'] == '1'])
    common_stat['Games with 2 players'] = len([game for game in games if game['Mode'] == '2'])
    from pprint import pprint
    pprint(common_stat)
