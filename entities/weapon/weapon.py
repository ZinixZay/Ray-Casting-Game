import pygame

from settings import HEIGHT, HALF_WIDTH


class Weapon:
    def __init__(self, param):
        self.param = param
        self.name = param['name']
        self.numbers_bullets = param['numbers_bullets']
        self.gun_magazine = param['gun_magazine']
        self.shot_length = param['shot_length']
        self.shot_count = 0
        self.bullet = self.gun_magazine

        self.base_texture = pygame.image.load(param['base_sprite']).convert_alpha()
        self.miniature = pygame.image.load(param['miniature']).convert_alpha()

    @property
    def get_bullet_str(self):
        return f'{self.bullet}/{self.gun_magazine}'

    def draw(self, screen):
        if self.shot_count > 0:
            self.shot_count -= 1
        screen.blit(self.base_texture, (HALF_WIDTH - self.base_texture.get_rect().width // 2,
                                        HEIGHT - self.base_texture.get_rect().height))

    def fire(self):
        if self.bullet > 0 and self.shot_count == 0:
            self.shot_count = self.shot_length
            self.bullet -= 1

    def recharge(self):
        if self.numbers_bullets > 0 and self.bullet < self.gun_magazine:
            bullet_prev = self.bullet
            if self.numbers_bullets > self.gun_magazine:
                self.bullet = self.gun_magazine
            else:
                self.bullet = self.numbers_bullets

            self.numbers_bullets = max(self.numbers_bullets - (self.gun_magazine - bullet_prev), 0)
