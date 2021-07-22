#! python

"""
Game: Tic-tac-toe.
"""

from cmd_game.tic_tac_toe.settings import read_setting, save_settings, default_setting, sm, input_set
from cmd_game.rendering import rend_menu, clr
from cmd_game.tic_tac_toe.game import run_game
from cmd_game.tic_tac_toe.statistics import show_stat
import keyboard
import time


FPS = 5

save_settings(default_setting)  # while debug
settings = read_setting()
mode = '1'
# '1' - Comp VS Player;
# '2' - Player 1 VS Player 2;


menu = [sm['main']]
selected_point = 0

last_key = None
exit_key = False
pause_key = False
play_key = False


def main():
    global play_key, exit_key, settings
    while True:
        if not pause_key:
            clr(rend_menu(menu[-1], settings, selected_point))
            time.sleep(1/FPS)
            keyboard.hook(check_pressed_keys)
        if exit_key:
            clr('Setting saved.\nPowered by Efi-fi.')
            save_settings(settings)
            exit()
        if play_key:
            run_game(settings, mode)
            play_key = False


def key_down():
    global selected_point, menu
    if selected_point < len(menu[-1]) - 1:
        selected_point += 1
    else:
        selected_point = 0


def key_up():
    global selected_point, menu
    if selected_point > 0:
        selected_point -= 1
    else:
        selected_point = len(menu[-1]) - 1


def key_esc():
    global selected_point, menu, exit_key
    if len(menu) < 2:
        exit_key = True
    else:
        selected_point = 0
        menu.pop()


def check_pressed_keys(event):
    """
    Check keys and performing actions according event.
    """
    global selected_point, last_key, play_key, mode, settings, pause_key
    if not last_key or (event.name != last_key.name) or (event.event_type == 'down' and last_key.event_type == 'up'):
        # processing events
        if event.name == 'down':
            key_down()
        elif event.name == 'up':
            key_up()
        elif event.name == 'esc':
            key_esc()
        elif event.name == 'space':
            # processing selected item
            if menu[-1][selected_point] == 'Exit':
                key_esc()
            elif menu[-1][selected_point] == 'Back':
                menu.pop()
                selected_point = 0
            elif menu[-1][selected_point].lower() in sm:
                menu.append(sm[menu[-1][selected_point].lower()])
                selected_point = 0
            elif menu[-1][selected_point] == 'One player':
                mode = '1'
                play_key = True
            elif menu[-1][selected_point] == 'Two players':
                mode = '2'
                play_key = True
            elif menu[-1][selected_point] == 'Statistics':
                pause_key = True
                clr()
                show_stat()
                input('Press Enter for Back\n')
                pause_key = False
            else:
                pause_key = True
                input_set(settings, menu, selected_point)
                pause_key = False
    last_key = event


if __name__ == '__main__':
    main()
else:
    print('This module is not for import!')
