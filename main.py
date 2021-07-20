"""
Game: Tic-tac-toe.
"""

from settings import read_setting, save_settings, default_player, default_setting
from statistics import read_statistics, save_statistics, gen_game_stats
from rendering import rend_board, clr
from comp import make_move as comp_move
import random as rnd

menu = {'main': ['Play', 'Setting', 'Exit'],
        'play': ['One player', 'Two players', 'Back'],
        'settings': list(default_setting) + ['Back'],
        'level': ['Low', 'Medium', 'Hard', 'Back'],
        'who first': ['Comp', 'Player', 'Random', 'Back'],
        }


def main():
    #curr_menu = menu['main']
    save_settings(default_setting)
    settings = read_setting()
    statistics = read_statistics()
    mode = def_mode()
    print(mode)
    if mode in '12':
        settings['Player 1'] = def_player(1)
        if mode == '2':
            settings['Player 2'] = def_player(2)
    board = [' ' for i in range(9)]
    #print(settings)
    #print(statistics)

    print('Start game!')
    game_stats = gen_game_stats(settings, mode)
    game_stats['First'] = def_who_first(settings, mode)
    print(rend_board(board))
    moves = 0
    active_player = game_stats['First']
    inactive_player = def_inactive_player(active_player, mode)
    while True:
        if active_player == 'Comp':
            cell = comp_move(board, game_stats['Level'])
        else:
            cell = player_move(board, game_stats['Player 1'])

        if active_player == game_stats['First']:
            board[cell] = 'X'
        else:
            board[cell] = 'O'
        moves += 1
        if check_win(board):
            game_stats['Winner'] = active_player
            game_stats['Moves'] = moves
            print(rend_board(board))
            print(f'Win {active_player}: {game_stats[active_player]}!')
            break
        if moves >= 9:
            game_stats['Moves'] = moves
            print(rend_board(board))
            print(f'DRAW!')
            break


        print(rend_board(board))
        active_player, inactive_player = inactive_player, active_player


def check_win(b):
    for i in range(3):
        if b[i*3] == b[i*3+1] == b[i*3+2] and (b[i*3] != ' '):  # horizontal lines
            return True
        if b[i] == b[i+3] == b[i+6] and (b[i] != ' '):  # vertical lines
            return True
    if (b[0] == b[4] == b[8] and b[0] != ' ') or (b[2] == b[4] == b[6] and b[2] != ' '):  # diagonals
        return True


def player_move(board, nick):
    try:
        cell = int(input(f'Choose empty cell, {nick}: -->'))
    except:
        cell = -1
    if cell in [i for i, char in enumerate(board) if char == ' ']:
        return cell
    else:
        print('The cell must be empty. Choose another cell.')
        return player_move(board, nick)


def def_inactive_player(active_player, mode):
    if active_player == 'Comp' or active_player == 'Player 2':
        return 'Player 1'
    elif mode == '1':
        return 'Comp'
    elif mode == '2':
        return 'Player 2'


def def_who_first(settings, mode):
    if mode == '1':
        if settings['Who first'] == 'Random':
            return rnd.choice(['Player 1', 'Comp'])
        elif settings['Who first'] == 'Player':
            return 'Player 1'
        else:
            return 'Comp'
    elif mode == '2':
        return rnd.choice(['Player 1', 'Player 2'])


def def_mode():
    """
    Allow choose game mode.
    :return: game mode:
    '1' - Comp VS Player;
    '2' - Player 1 VS Player 2;
    '3' - Comp 1 VS Comp 2;
    """
    mode = input('Hello, choose mode: 1 - Comp VS Player; 2 - Player 1 VS Player 2; 3 - Comp 1 VS Comp 2;\n-->')

    if mode in '123':
        return mode
    else:
        print(f'Incorrect mode: {mode}. Please, choose again.')
        return def_mode()  # Use recursion


def def_player(num: 'Number'):
    """

    :param num: Number of player
    :return: String: player nick
    """
    player = input(f'Please input nick for Player {num}: ')
    if player:
        return player
    else:
        return f'{default_player} {num}'


if __name__ == '__main__':
    main()
