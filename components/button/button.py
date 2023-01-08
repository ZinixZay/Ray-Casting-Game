import pygame

from paths import FONT_PATH
from settings import WHITE, BLACK, LIGHT_GRAY


class Button:
    def __init__(self, pos: tuple[int, int], size: tuple[int, int], texture, active_texture=False, title: str = '') -> None:
        self.pos = self.x, self.y = pos
        self.size = self.width, self.height = size
        self.title = title
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.texture = texture
        self.active_texture = active_texture
        self.font = pygame.font.Font(FONT_PATH + 'Fifaks10Dev1.ttf', 34)
        self.clicked = False

    def get_status(self) -> bool:
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return self.clicked

    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and self.active_texture:
            title = self.font.render(self.title, 0, WHITE)
            screen.blit(self.active_texture, (self.rect.x, self.rect.y))
        else:
            title = self.font.render(self.title, 0, LIGHT_GRAY)
            screen.blit(self.texture, (self.rect.x, self.rect.y))
        screen.blit(title, (self.rect.x + 26, self.rect.y + self.height // 2 - title.get_rect().height // 2))
