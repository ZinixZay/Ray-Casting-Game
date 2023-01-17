import numpy
import pygame

from entities.weapon.weapon import Weapon
from settings import *


class MainPlayer:
    def __init__(self, player_pos: tuple, weapon: Weapon, angle: int = 0, speed: int = 2) -> None:
        self.x, self.y = player_pos
        self.health_points = 100
        self.armor_points = 100
        self.weapon = weapon
        self.inventory = list()
        self.angle = angle
        self.speed = speed
        self.sensitivity = SENSITIVITY
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        self.shot = False
        self.collision_objs = list()
        self.entity_service = None
        self.immortal = 40
        self.immortal_count = 0

    @property
    def pos(self) -> tuple:
        return self.x, self.y

    @property
    def pos_normalize(self) -> tuple:
        return self.x/TILE, self.y/TILE

    def update_collision_objs(self, objs: list, entity_service) -> None:
        self.collision_objs = objs
        self.entity_service = entity_service

    def detect_collision(self, dx: float, dy: float) -> None:
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        collide_list = self.collision_objs + [i.rect for i in self.entity_service.entities if i.blocked]
        hit_indexes = next_rect.collidelistall(collide_list)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = collide_list[hit_index]
                delta_x += next_rect.right - hit_rect.left if dx > 0 else hit_rect.right - next_rect.left
                delta_y += next_rect.bottom - hit_rect.top if dy > 0 else hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 40:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy
        self.rect = next_rect

    def movement(self) -> None:
        self.keys_control()
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.angle %= DOUBLE_PI
        if self.immortal_count > 0:
            self.immortal_count -= 1
        pygame.event.clear()

    def keys_control(self) -> None:
        sin_a, cos_a = math.sin(self.angle), math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()

        if keys[pygame.K_w]:
            self.detect_collision(self.speed * cos_a, self.speed * sin_a)
        if keys[pygame.K_s]:
            self.detect_collision(-self.speed * cos_a, -self.speed * sin_a)
        if keys[pygame.K_a]:
            self.detect_collision(self.speed * sin_a, -self.speed * cos_a)
        if keys[pygame.K_d]:
            self.detect_collision(-self.speed * sin_a, self.speed * cos_a)

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    def mouse_control(self) -> None:
        self.shot = False
        if pygame.mouse.get_pressed()[0]:
            self.shot = self.weapon.fire()
        elif pygame.mouse.get_pressed()[2]:
            self.weapon.recharge()
        self.angle += numpy.clip((pygame.mouse.get_rel()[0]) / 200, -0.2, .2)

    def damage(self, damage):
        if self.immortal_count == 0:
            if self.armor_points > 0:
                self.armor_points -= int(damage/100*80)
                if self.armor_points < 0: self.armor_points = 0
                self.health_points -= int(damage/100*20)
            else:
                self.health_points -= int(damage)
            self.immortal_count = self.immortal

    def heal(self, points):
        self.health_points = min(self.health_points + points, 100)

    @staticmethod
    def is_moving() -> bool:
        keys = pygame.key.get_pressed()
        return any([keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_a], keys[pygame.K_d]])
