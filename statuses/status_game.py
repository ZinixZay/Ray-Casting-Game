from enum import Enum


class STATUS_GAME(Enum):
    MENU_START = 'MENU_START'
    MENU_PAUSE = 'MENU_PAUSE'
    MENU_WIN = 'MENU_WIN'
    MENU_LOSE = 'MENU_LOSE'
    GAME_PROCESS = 'GAME_PROCESS'
    GAME_PROCESS_RANDOM = 'GAME_PROCESS_RANDOM'
    GAME_PROCESS_RESTART = 'GAME_PROCESS_RESTART'
    GAME_PROCESS_CONTINUE = 'GAME_PROCESS_CONTINUE'
    EXIT = 'EXIT'
