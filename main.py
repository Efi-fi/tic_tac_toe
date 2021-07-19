"""
Игра крестики-нолики.

ТЗ:
1) 2 режима игры: 2 чел, чел против компа
2) комп имеет 3 уровня сложности
3) всё в консоле
"""

from settings import read_setting



menu = {'main': ['Play', 'Setting', 'Exit'],
        'play': ['One player', 'Two players'],
        'settings': ['Level', 'Who first', 'Size'],
        'level': ['Low', 'Medium', 'Hard'],
        'who first': ['Comp', 'Player', 'Random'],
        }


def main():
    curr_menu = menu['main']
    settings = read_setting()
    while True:
        print(head)
        for i, point in enumerate(curr_menu):
            print(get_txt_line(point + ' -> ' + str(i)))
        print(foot)


def get_txt_line(text='', num=None):
    if len(text) <= 78:
        filler = ' '
        offset = (78 - len(text)) // 2
        line = '|'
        line += (filler * offset) + text + (offset * filler)
        if len(line) == 78:
            line += filler
        line += '|'
        return line


if __name__ == '__main__':
    main()
