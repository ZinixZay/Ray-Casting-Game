import pygame.font

from components.button.button import Button
from components.menu_start.config import BUTTONS
from core.status_game import STATUS_GAME
from paths import FONT_PATH
from settings import LIGHT_GRAY2


class MenuStart:
    def __init__(self, btn_texture, btn_active_texture, background_image):
        self.title = 'No Return'
        self.background_image = background_image
        self.font = pygame.font.Font(FONT_PATH +'\\GULAG Pavljenko.otf', 100)
        self.buttons = {Button(pos, size, btn_texture, btn_active_texture, title=name): status for pos, size, name, status in BUTTONS}

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        text = self.font.render(self.title, 0, LIGHT_GRAY2)
        screen.blit(text, (100, 100))
        for btn in self.buttons:
            btn.draw(screen)

    def get_status(self) -> bool | STATUS_GAME:
        for btn in self.buttons:
            if btn.get_status():
                return self.buttons[btn]
        return False
    