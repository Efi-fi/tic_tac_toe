"""

"""

import os


def clr():
    os.system('cls')


max_len = 80

filler = '*'
top = '|-tic-tac-toe' + '-' * (max_len-30) + 'Powered by Efi-fi-|'
bottom = '|' + '-' * (max_len-2) + '|'



def rend_menu(menu):
    """
    Функция для рендеринга меню в консоле.
    """


def rend_board(board: list, help_board=True):
    """
    Функция для вывода игрового поля в консоль.

    :param board: список значений клеток поля
    :return: поле в виде текста
    """
    # board_txt = top + get_txt_line()
    board_txt = ''
    for row in range(3):
        board_txt += '\n' + '-' * 7 + '\n|'
        for col in range(3):
            board_txt += f'{board[row*3+col]}|'
    board_txt += '\n' + '-' * 7 + '\n'
    return board_txt


def get_txt_line(text='', num=None):
    if len(text) <= (max_len-2):
        offset = (max_len - 2 - len(text)) // 2
        line = '|'
        line += (filler * offset) + text + (offset * filler)
        if len(line) == (max_len-2):
            line += filler
        line += '|'
        return line

