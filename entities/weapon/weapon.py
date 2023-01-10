import pygame

from settings import HEIGHT, HALF_WIDTH


class Weapon:
    def __init__(self, param):
        self.param = param
        self.name = param['name']
        self.base_texture = pygame.image.load(param['base_sprite']).convert_alpha()

    def draw(self, screen):
        screen.blit(self.base_texture, (HALF_WIDTH-self.base_texture.get_rect().width//2,
                                        HEIGHT-self.base_texture.get_rect().height))

    def fire(self):
        pass

    def recharge(self):
        pass
