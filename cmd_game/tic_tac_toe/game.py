from cmd_game.tic_tac_toe.statistics import read_statistics, save_statistics, gen_game_stats
from cmd_game.tic_tac_toe.comp import make_move as comp_move
from cmd_game.tic_tac_toe.settings import modes
from cmd_game.rendering import rend_board, clr
import random as rnd


def run_game(settings, mode):
    """
    Start tic tac toe game.

    Use setting and mode. Save game statistics in JSON file.
    """

    statistics = read_statistics()
    board = [' ' for _ in range(9)]
    clr()
    value = input(f'Game settings:\n'
                  f'\tMode:\t{modes[mode]}\n'
                  f'\tPlayer 1 nick:\t{settings["Player 1"]}\n'
                  f'\tPlayer 2 nick:\t{settings["Player 2"]}\n'
                  f'\tLevel:\t{settings["Level"]}\n'
                  f'For starting press Enter,\n'
                  f'else input someone that back in menu and change setting.')
    if value:  # if value then return to menu
        return

    game_stats = gen_game_stats(settings, mode)  # dict for accumulate statistics for this game
    game_stats['First'] = def_who_first(settings, mode)  # define beginner
    clr(rend_board(board))  # clear terminal and show empty board
    moves = 0  # counter for moves

    active_player = game_stats['First']  # active player -> beginner
    inactive_player = def_inactive_player(active_player, mode)  # inactive player -> second player (according mode)

    while True:  # One cycle per move
        # Make a move
        if active_player == 'Comp':
            cell = comp_move(board, game_stats['Level'])  # comp select cell
        else:
            cell = player_move(board, active_player, game_stats[active_player])  # player input selected cell

        # Define char for filling cell
        if active_player == game_stats['First']:
            board[cell] = 'X'  # beginner moved by X
        else:
            board[cell] = 'O'

        moves += 1
        clr(rend_board(board))  # upd board after moving

        if check_win(board):
            game_stats['Winner'] = active_player
            game_stats['Moves'] = moves
            clr(rend_board(board))
            print(f'Win {active_player}: {game_stats[active_player]}!')
            if 'Games' not in statistics:
                statistics['Games'] = []
            statistics['Games'].append(game_stats)
            input('Press Enter then return in menu')
            break

        if moves >= 9:
            game_stats['Moves'] = moves
            clr(rend_board(board))
            print(f'DRAW!')
            if 'Games' not in statistics:
                statistics['Games'] = []
            statistics['Games'].append(game_stats)
            input('Press Enter then return in menu')
            break

        active_player, inactive_player = inactive_player, active_player  # swap players

    save_statistics(statistics)


def check_win(b):
    """
    Check win's combinations.
    """
    for i in range(3):
        if b[i * 3] == b[i * 3 + 1] == b[i * 3 + 2] and (b[i * 3] != ' '):  # horizontal lines
            return True
        if b[i] == b[i + 3] == b[i + 6] and (b[i] != ' '):  # vertical lines
            return True
    if (b[0] == b[4] == b[8] and b[0] != ' ') or (b[2] == b[4] == b[6] and b[2] != ' '):  # diagonals
        return True


def player_move(board, player, nick):
    """
    Allow input selected cell by player.
    """
    try:
        cell = int(input(f'{player}: Choose empty cell, {nick}: -->'))
    except:
        cell = -1
    if cell in [i for i, char in enumerate(board) if char == ' ']:
        return cell
    else:
        print('The cell must be empty. Choose another cell.')
        return player_move(board, player, nick)


def def_inactive_player(active_player, mode):
    """
    Define inactive player.
    """
    if active_player == 'Comp' or active_player == 'Player 2':
        return 'Player 1'
    elif mode == '1':
        return 'Comp'
    elif mode == '2':
        return 'Player 2'


def def_who_first(settings, mode):
    """
    Define beginner according settings.
    """
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

    """
    mode = input('Hello, choose mode: 1 - Comp VS Player; 2 - Player 1 VS Player 2; 3 - Comp 1 VS Comp 2;\n-->')
    if mode in '123':
        return mode
    else:
        print(f'Incorrect mode: {mode}. Please, choose again.')
        return def_mode()  # Use recursion while correct input
