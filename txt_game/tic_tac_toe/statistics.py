"""
Statistics:
{
Games:[game1, game2, ... ],
}
"""

import json
import numpy as np
import platform
import datetime as dt
from txt_game.tic_tac_toe.settings import default_setting


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


def gen_common_stat(filename=default_setting['Statistic filename']):
    """
        Generating statistics.
        """
    stats = read_statistics(filename)
    games = stats['Games']
    common_stat = dict()
    common_stat['Games'] = len(games)
    common_stat['Games with comp'] = len([game for game in games if game['Mode'] == '1'])
    common_stat['Games with 2 players'] = len([game for game in games if game['Mode'] == '2'])
    common_stat['Players'] = {}
    common_stat['Moves'] = {5: 0,
                            6: 0,
                            7: 0,
                            8: 0,
                            9: 0}
    player_stat = {'Games': 0,
                   'Wins': 0,
                   'Draws': 0,
                   'Fails': 0}
    for game in games:
        if game['Player 1'] not in common_stat['Players']:
            common_stat['Players'][game['Player 1']] = player_stat.copy()
        if game['Player 2'] not in common_stat['Players']:
            common_stat['Players'][game['Player 2']] = player_stat.copy()
        if game['Comp'] not in common_stat['Players']:
            common_stat['Players'][game['Comp']] = player_stat.copy()

        upd_player_stat(common_stat, game, 'Player 1')
        if game['Mode'] == '1':
            upd_player_stat(common_stat, game, 'Comp')
        else:
            upd_player_stat(common_stat, game, 'Player 2')

        common_stat['Moves'][game['Moves']] += 1

    return common_stat


def show_stat(filename=default_setting['Statistic filename']):

    # moves_stat = get_seq_stat(common_stat['Moves'].keys(), common_stat['Moves'].values())
    # visualize_seq(moves_stat)
    common_stat = gen_common_stat(filename)
    from pprint import pprint
    pprint(common_stat)


def upd_player_stat(common_stat, game, player):
    """
    Update player statistics.
    """
    common_stat['Players'][game[player]]['Games'] += 1
    if game['Winner'] == player:
        common_stat['Players'][game[player]]['Wins'] += 1
    elif game['Winner']:
        common_stat['Players'][game[player]]['Fails'] += 1
    else:
        common_stat['Players'][game[player]]['Draws'] += 1


def get_seq_stat(xlst, ylst):
    """
    Generate dict with sequence statistics.
    """
    stat = dict()
    stat['xlst'] = np.array(list(xlst))
    stat['ylst'] = np.array(list(ylst))
    stat['avg'] = np.average(stat['ylst'])
    stat['median'] = np.median(stat['ylst'])
    stat['std'] = np.std(stat['ylst'])

    return stat
