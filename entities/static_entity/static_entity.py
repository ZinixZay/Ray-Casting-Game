import pygame

from core.utils.utils import get_sprite_angles
from entities.main_player.main_player import MainPlayer
from settings import *
from collections import deque


class StaticEntity:
    def __init__(self, parameters: dict, pos: tuple[float, float], angle: int = 0) -> None:
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
        self.side = parameters['side']
        self.health_point = parameters['heath_point']
        self.animation_count = 0
        self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.pos = self.x - self.side // 2, self.y - self.side // 2
        self.angle = angle
        self.rect = pygame.Rect(*self.pos, self.side, self.side)
        if self.viewing_angles:
            self.sprite_angles = list(map(frozenset, get_sprite_angles(self.angle)))
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.objects)}

    def is_on_fire(self, player):
        if CENTER_RAY - self.side // 2 < self.current_ray < CENTER_RAY + self.side // 2 and self.blocked:
            return self.distance(player), self.proj_height
        return float('inf'), None

    def distance(self, player):
        dx, dy = self.x - player.x, self.y - player.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def object_locate(self, player: MainPlayer) -> tuple:
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = self.distance(player)
        
        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        self.current_ray = CENTER_RAY + int(gamma / DELTA_ANGLE)
        distance_to_sprite *= math.cos(HALF_FOV - self.current_ray * DELTA_ANGLE)

        if 0 <= self.current_ray + FAKE_RAYS <= FAKE_RAYS_RANGE and distance_to_sprite > 30:
            self.proj_height = min(int(PROJ_COEFF / distance_to_sprite * self.scale), DOUBLE_HEIGHT)
            half_proj_height = self.proj_height // 2
            shift = half_proj_height * self.shift
            if self.viewing_angles:
                if theta < 0:
                    theta += DOUBLE_PI

                for angles in self.sprite_angles:
                    if min(360 - int(math.degrees(theta)), 359) in angles:
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

            sprite = pygame.transform.scale(sprite_object, (self.proj_height, self.proj_height))
            return distance_to_sprite, sprite, \
                    (self.current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
        return False, False, False

    def update_pos(self, pos: tuple[float, float]) -> None:
        self.x, self.y = list(map(lambda x: x * TILE, pos))

    def update_angle(self, angle: int) -> None:
        self.angle = angle
        if self.viewing_angles:
            self.sprite_angles = list(map(frozenset, get_sprite_angles(self.angle)))
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.objects)}
