#! python

"""
Game: Tic-tac-toe.
"""

from cmd_game.tic_tac_toe.settings import read_setting, save_settings, default_setting, menu as sm
from cmd_game.rendering import rend_menu, clr
from cmd_game.tic_tac_toe.game import run_game
import keyboard
import time

mode = '1'
# '1' - Comp VS Player;
# '2' - Player 1 VS Player 2;
# '3' - Comp 1 VS Comp 2;


menu = [sm['main']]
selected_point = 0

last_key = None
exit_key = False
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
    global selected_point, last_key, play_key, mode
    if not last_key or (event.name != last_key.name) or (event.event_type == 'down' and last_key.event_type == 'up'):
        if event.name == 'down':
            key_down()
        elif event.name == 'up':
            key_up()
        elif event.name == 'esc':
            key_esc()
        elif event.name == 'space':
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
    last_key = event


def main():
    global play_key
    save_settings(default_setting)  # while debug
    settings = read_setting()
    while True:
        clr(rend_menu(menu[-1], selected_point))
        time.sleep(0.2)
        keyboard.hook(check_pressed_keys)
        if exit_key:
            exit()
        if play_key:
            keyboard.unhook_all()
            run_game(settings, mode)
            play_key = False


if __name__ == '__main__':
    main()
