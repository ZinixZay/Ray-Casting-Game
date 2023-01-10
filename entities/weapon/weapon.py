import pygame

from settings import HEIGHT, HALF_WIDTH


class Weapon:
    def __init__(self, param):
        self.param = param
        self.shot = 0
        self.shot_animation_count = 0
        self.shot_animation_speed = 10
        self.name = param['name']
        self.numbers_bullets = param['numbers_bullets']
        self.gun_magazine = param['gun_magazine']
        self.bullet = self.gun_magazine

        self.base_texture = pygame.image.load(param['base_sprite']).convert_alpha()
        self.miniature = pygame.image.load(param['miniature']).convert_alpha()

    @property
    def get_bullet_str(self):
        return f'{self.bullet}/{self.gun_magazine}'

    def draw(self, screen):
        # if self.shot:
        #     self.shot_animation_count += 1
        #     if self.shot_animation_count == self.shot_animation_speed:
        #         self.weapon_shot_animation.rotate(-1)
        #         self.shot_animation_count = 0
        #         self.shot_length_count += 1
        #         self.shot_animation_trigger = False
        #     if self.shot_length_count == self.shot_length:
        #         self.player.shot = False
        #         self.shot_length_count = 0
        #         self.sfx_length_count = 0
        #         self.shot_animation_trigger = True
        # else:
            screen.blit(self.base_texture, (HALF_WIDTH - self.base_texture.get_rect().width // 2,
                                        HEIGHT - self.base_texture.get_rect().height))

    def fire(self):
        if self.bullet > 0:
            self.bullet -= 1

    def recharge(self):
        if self.numbers_bullets > 0 and self.bullet < self.gun_magazine:
            bullet_prev = self.bullet
            if self.numbers_bullets > self.gun_magazine:
                self.bullet = self.gun_magazine
            else:
                self.bullet = self.numbers_bullets

            self.numbers_bullets = max(self.numbers_bullets - (self.gun_magazine - bullet_prev), 0)
