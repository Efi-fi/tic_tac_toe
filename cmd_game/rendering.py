"""

"""

import os
from termcolor import colored

formats = {
    'norm': '\x1b[0m',
    'back': '\x1b[4;41m',
    'selected': '\x1b[42;1m',
    'board': '\x1b[1m'
}


def clr(text=None):
    os.system('cls')
    if text:
        print(text, end='')


max_len = 80

filler = ' '
top = '+' + '-'*(max_len-2) + '+'
bottom = '+' + '-'*(max_len - 2) + '+'



def rend_board(board: list, help_board=True):
    """

    """
    board_txt = formats['board']
    for row in range(3):
        for col in range(3):
            board_txt += f'{board[row * 3 + col]}'
            board_txt += '|' if col < 2 else '\n'
        board_txt += '-+-+-\n' if row < 2 else formats['norm'] + '\n'

    return board_txt


def get_menu_line(point=''):
    if len(point) <= (max_len - 2):
        offset = (max_len - 2 - len(point)) // 2
        line = '|'
        line += (filler * offset) + point + (offset * filler)
        if len(line) == (max_len - 2):
            line += filler
        line += '|'
        return line


def rend_menu(points, selected=0):
    """

    """
    menu_txt = top + '\n'
    for i, point in enumerate(points):
        if i == selected:
            point = f'>>> {point} <<<'
        menu_txt += get_menu_line(point) + '\n'
    return menu_txt + bottom
