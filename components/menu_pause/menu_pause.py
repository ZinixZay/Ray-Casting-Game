from components.button.button import Button
from core.status_game import STATUS_GAME


class MenuPause:
    def __init__(self, btn_image, background_image):
        self.title = 'Pause'
        self.background_image = background_image
        self.buttons = {
            Button((600, 400), (300, 80), btn_image, 'Resume'): STATUS_GAME.GAME_PROCESS,
            Button((600, 500), (300, 80), btn_image, 'Exit Main Menu'): STATUS_GAME.MENU_START,
            Button((600, 600), (300, 80), btn_image, 'Exit Game'): STATUS_GAME.EXIT,
        }

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        for btn in self.buttons:
            btn.draw(screen)

    def get_status(self) -> bool | STATUS_GAME:
        for btn in self.buttons:
            if btn.get_status():
                print(self.buttons[btn])
                return self.buttons[btn]
        return False
