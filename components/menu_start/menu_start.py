import pygame.font

from components.button.button import Button
from components.menu_start.config import BUTTONS
from core.status_game import STATUS_GAME
from paths import FONT_PATH
from settings import RED, LIGHT_GRAY, HALF_HEIGHT


class MenuStart:
    def __init__(self, btn_image, background_image):
        self.title = 'No Return'
        self.background_image = background_image
        self.font = pygame.font.Font(FONT_PATH +'\\GULAG Pavljenko.otf', 100)
        self.buttons = {Button(pos, size, btn_image, name): status for pos, size, name, status in BUTTONS}

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        text = self.font.render(self.title, 0, LIGHT_GRAY)
        screen.blit(text, (HALF_HEIGHT-20, 100))
        for btn in self.buttons:
            btn.draw(screen)

    def get_status(self) -> bool | STATUS_GAME:
        for btn in self.buttons:
            if btn.get_status():
                return self.buttons[btn]
        return False
