from components.button.button import Button
from components.menu_pause.config import BUTTONS
from core.status_game import STATUS_GAME


class MenuPause:
    def __init__(self, btn_image, background_image):
        self.title = 'Pause'
        self.background_image = background_image
        self.buttons = {Button(pos, size, btn_image, name): status for pos, size, name, status in BUTTONS}


    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        for btn in self.buttons:
            btn.draw(screen)

    def get_status(self) -> bool | STATUS_GAME:
        for btn in self.buttons:
            if btn.get_status():
                return self.buttons[btn]
        return False
