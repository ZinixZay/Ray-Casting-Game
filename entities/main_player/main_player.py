import numpy
import pygame
from settings import *


class MainPlayer:
    def __init__(self, player_pos: tuple, angle: int = 0, speed: int = 2) -> None:
        self.x, self.y = player_pos
        self.health_points = 100
        self.inventory = list()
        self.angle = angle
        self.speed = speed
        self.sensitivity = SENSITIVITY
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        self.collision_objs = list()

    @property
    def pos(self) -> tuple:
        return self.x, self.y

    def update_collision_objs(self, objs: list) -> None:
        self.collision_objs = objs

    def detect_collision(self, dx: float, dy: float) -> None:
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.collision_objs)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.collision_objs[hit_index]
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

    def movement(self) -> None:
        self.keys_control()
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.angle %= DOUBLE_PI

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
        self.angle += numpy.clip((pygame.mouse.get_rel()[0]) / 200, -0.2, .2)
