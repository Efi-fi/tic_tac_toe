"""
Statistics:
Games:[
{
Game time : ...,
Mode: 1..3,
Player 1: nick 1,
Player 2: nick 2,
Level: ...,
Winner: Comp or Player 1 or Player 2,
First: Comp or Player 1 or Player 2,
Moves: 0..9,
}, ...]
"""

import json
import platform
import datetime as dt
from settings import default_setting


def read_statistics(filename=default_setting['Statistic filename']):
    stats = {}
    try:
        with open(filename) as json_file:
            stats = json.load(json_file)
    except:
        save_statistics(stats)
    finally:
        return stats


def save_statistics(statistics, filename=default_setting['Statistic filename']):
    with open(filename, 'w') as json_file:
        json.dump(statistics, json_file)


def gen_game_stats(settings: dict, mode: str):
    game_stats = {
        'Game time': dt.datetime.now(),
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
