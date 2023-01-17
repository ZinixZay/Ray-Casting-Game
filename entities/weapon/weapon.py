from collections import deque

import pygame

from settings import HEIGHT, HALF_WIDTH


class Weapon:
    def __init__(self, param):
        self.param = param
        self.name = param['name']

        self.damage = param['damage']

        self.numbers_bullets = param['numbers_bullets']
        self.gun_magazine = param['gun_magazine']
        self.bullet = self.gun_magazine

        self.shot_length = param['shot_length']
        self.shot_count = 0

        self.animation_shot_speed = param['animation_shot_speed']
        self.animation_shot_count = 0

        self.base_texture = pygame.image.load(param['base_sprite']).convert_alpha()
        self.exhausted_texture = pygame.image.load(param['exhausted_sprite']).convert_alpha()

        self.shot_animation = deque([pygame.image.load(i).convert_alpha() for i in param['animation_shot'].copy()])
        self.miniature = pygame.image.load(param['miniature']).convert_alpha()

    @property
    def get_bullet_str(self):
        return f'{self.bullet}/{self.gun_magazine}'

    def draw(self, screen):
        if self.shot_count > 0:
            self.shot_count -= 1
            self.animation_shot_count += 1
            if self.animation_shot_count == self.animation_shot_speed:
                self.animation_shot_count = 0
                self.shot_animation.rotate(-1)
            screen.blit(self.shot_animation[0], (HALF_WIDTH - self.shot_animation[0].get_rect().width // 2,
                                                    HEIGHT - self.shot_animation[0].get_rect().height))
        else:
            if self.bullet > 0:
                screen.blit(self.base_texture, (HALF_WIDTH - self.base_texture.get_rect().width // 2,
                                            HEIGHT - self.base_texture.get_rect().height))
            else:
                screen.blit(self.exhausted_texture, (HALF_WIDTH - self.exhausted_texture.get_rect().width // 2,
                                                HEIGHT - self.exhausted_texture.get_rect().height))

    def fire(self) -> bool:
        if self.bullet > 0 and self.shot_count == 0:
            self.shot_count = self.shot_length
            self.bullet -= 1
            return True
        return False

    def recharge(self):
        if self.numbers_bullets > 0 and self.bullet < self.gun_magazine:
            need_bullet = self.gun_magazine - self.bullet
            remains = self.numbers_bullets - need_bullet
            if remains > 0:
                self.numbers_bullets = remains
                self.bullet = self.gun_magazine
            else:
                self.numbers_bullets = 0
                self.bullet = self.gun_magazine + remains
