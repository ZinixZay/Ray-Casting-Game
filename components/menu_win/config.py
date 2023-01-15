from core.status_game import STATUS_GAME
from settings import WIDTH, HEIGHT

BUTTONS = [
    ((20, HEIGHT-110), (300, 90), 'NEXT_LEVEL', STATUS_GAME.GAME_PROCESS),
    ((WIDTH-320, HEIGHT-110), (300, 90), 'Exit', STATUS_GAME.EXIT)
]
