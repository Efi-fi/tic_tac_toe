"""
Functions for rendering structures in console.
"""

import os


formats = {
    'norm': '\x1b[0m',
    'back': '\x1b[4;40m',
    'selected': '\x1b[34;1m',
    'board': '\x1b[1m',
    'blinked': '\x1b[31m',
}


def clr(text=None):
    """
    Clear console and print text if received.
    """
    os.system('cls')
    if text:
        print(text, end='')


max_len = 40

filler = ' '
top = '+' + '-'*(max_len-2) + '+'
bottom = '+' + '-'*(max_len - 2) + '+'


def rend_board(board: list):
    """
    Rendering board for tic tac toe.
    """
    board_txt = formats['board']
    for row in range(3):
        for col in range(3):
            board_txt += f'{board[row * 3 + col]}'
            board_txt += '|' if col < 2 else '\n'
        board_txt += '-+-+-\n' if row < 2 else formats['norm'] + '\n'

    return board_txt


def get_menu_line(point='', line_len=max_len):
    """
    Return menu point line.
    """
    if len(point) <= (line_len - 2):
        offset = (line_len - 2 - len(point)) // 2
        line = '|'
        line += (filler * offset) + point + (offset * filler)
        if len(line) == (line_len - 2):
            line += filler
        line += '|'
        return line


def rend_menu(points, settings, selected=0):
    """
    Return menu text.
    """
    menu_txt = top + '\n'
    for i, point in enumerate(points):
        line_len = max_len
        if point == settings['Level'] and points[0] == 'Low':
            point = f'{formats["selected"]}{point}{formats["norm"]}'
            line_len += 11
        elif point == settings['Who first'] and points[0] == 'Comp':
            point = f'{formats["selected"]}{point}{formats["norm"]}'
            line_len += 11
        elif point == 'Back':
            point = f'{formats["back"]}{point}{formats["norm"]}'
            line_len += 11

        if i == selected:
            point = f'>>> {formats["blinked"]}{point}{formats["norm"]} <<<'
            line_len += 9

        menu_txt += get_menu_line(point, line_len) + '\n'
    return menu_txt + bottom
