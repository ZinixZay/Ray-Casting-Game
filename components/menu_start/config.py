from statuses.status_game import STATUS_GAME

BUTTONS = [
    ((100, 285), (300, 90), 'Continue', STATUS_GAME.GAME_PROCESS_CONTINUE),
    ((100, 370), (300, 90), 'Start', STATUS_GAME.GAME_PROCESS),
    ((100, 455), (300, 90), 'Start random', STATUS_GAME.GAME_PROCESS_RANDOM),
    ((100, 540), (300, 90), 'Exit', STATUS_GAME.EXIT)
]
