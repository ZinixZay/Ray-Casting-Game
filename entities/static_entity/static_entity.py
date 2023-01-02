from pprint import pprint

import pygame

from core.utils.utils import get_sprite_angles
from settings import *
from collections import deque


class StaticEntity:
    def __init__(self, parameters, pos):
        self.param = parameters
        if parameters['viewing_angles']:
            self.objects = [pygame.image.load(i).convert_alpha() for i in parameters['sprites'].copy()]
        self.object = pygame.image.load(parameters['sprites'][0]).convert_alpha()
        self.viewing_angles = parameters['viewing_angles']
        self.angle = parameters['angle']
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = deque([pygame.image.load(i).convert_alpha() for i in parameters['animation'].copy()])
        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.blocked = parameters['blocked']
        self.side = 30
        self.animation_count = 0
        self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.pos = self.x - self.side // 2, self.y - self.side // 2
        if self.viewing_angles:
            self.sprite_angles = list(map(frozenset, get_sprite_angles(self.angle)))
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.objects)}

    def object_locate(self, player):
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        distance_to_sprite *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        fake_ray = current_ray + FAKE_RAYS
        if 0 <= fake_ray <= FAKE_RAYS_RANGE and distance_to_sprite > 30:
            proj_height = min(int(PROJ_COEFF / distance_to_sprite * self.scale), DOUBLE_HEIGHT)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift
            if self.viewing_angles:
                if theta < 0:
                    theta += DOUBLE_PI
                theta = min(360 - int(math.degrees(theta)), 359)

                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break

            sprite_object = self.object
            if self.animation and distance_to_sprite < self.animation_dist:
                sprite_object = self.animation[0]
                if self.animation_count < self.animation_speed:
                    self.animation_count += 1
                else:
                    self.animation.rotate()
                    self.animation_count = 0

            sprite_pos = (current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            sprite = pygame.transform.scale(sprite_object, (proj_height, proj_height))
            return distance_to_sprite, sprite, sprite_pos
        return False, False, False

    def update_pos(self, pos: tuple[float, float]) -> None:
        self.x, self.y = pos[0] * TILE, pos[1] * TILE

    def update_angle(self, angle: int) -> None:
        self.angle = angle
        if self.viewing_angles:
            self.sprite_angles = list(map(frozenset, get_sprite_angles(self.angle)))
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.objects)}

