from core.status_game import STATUS_GAME
from settings import HALF_WIDTH

BUTTONS = [
    ((HALF_WIDTH-150, 350), (300, 90), 'RESTART', STATUS_GAME.GAME_PROCESS),
    ((HALF_WIDTH-150, 435), (300, 90), 'Exit Main Menu', STATUS_GAME.MENU_START),
    ((HALF_WIDTH-150, 520), (300, 90), 'Exit', STATUS_GAME.EXIT)
]
