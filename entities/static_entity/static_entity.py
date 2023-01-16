import pygame

from core.utils.utils import get_sprite_angles
from entities.main_player.main_player import MainPlayer
from settings import *
from collections import deque


class StaticEntity:
    def __init__(self, parameters: dict, pos: tuple[float, float], angle: int = 0) -> None:
        self.param = parameters
        self.type = parameters['type']
        if parameters['viewing_angles']:
            self.objects = [pygame.image.load(i).convert_alpha() for i in parameters['sprites'].copy()]
        self.object = pygame.image.load(parameters['sprites'][0]).convert_alpha()
        self.viewing_angles = parameters['viewing_angles']
        self.angle = parameters['angle']
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = deque([pygame.image.load(i).convert_alpha() for i in parameters['animation'].copy()])
        self.death_animation = deque([pygame.image.load(i).convert_alpha() for i in parameters['death_animation'].copy()])
        self.action_animation = deque([pygame.image.load(i).convert_alpha() for i in parameters['action_animation'].copy()])
        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.blocked = parameters['blocked']
        self.side = parameters['side']
        self.health_point = parameters['heath_point']
        self.animation_count = 0
        self.dead_animation_count = 0
        self.action_dist = parameters['action_dist']
        self.action_length = 0
        self.damage = parameters['damage']
        self.speed = parameters['speed']
        self.death = False
        self.action_trigger = False
        self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.pos = self.x - self.side // 2, self.y - self.side // 2
        self.angle = angle
        self.rect = pygame.Rect(*self.pos, self.side, self.side)
        self.chance = 0.40
        if self.viewing_angles:
            self.sprite_angles = list(map(frozenset, get_sprite_angles(self.angle)))
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.objects)}
        self.current_ray = 0

    def is_on_fire(self, player):
        if CENTER_RAY - self.side // 2 < self.current_ray < CENTER_RAY + self.side // 2 and self.blocked:
            return self.distance(player), self.proj_height
        return float('inf'), None

    def distance(self, player):
        dx, dy = self.x - player.x, self.y - player.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def object_locate(self, player: MainPlayer) -> tuple:
        dx, dy = self.x - player.x, self.y - player.y
        self.distance_to_sprite = self.distance(player)

        self.theta = math.atan2(dy, dx)
        gamma = self.theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI
        self.theta -= 1.4 * gamma

        self.current_ray = CENTER_RAY + int(gamma / DELTA_ANGLE)

        fake_ray = self.current_ray + FAKE_RAYS
        if 0 <= fake_ray <= FAKE_RAYS_RANGE and self.distance_to_sprite > 30:
            self.proj_height = min(int(PROJ_COEFF / self.distance_to_sprite), HEIGHT)
            sprite_width = int(self.proj_height * self.scale[0])
            sprite_height = int(self.proj_height * self.scale[1])
            half_sprite_width = sprite_width // 2
            half_sprite_height = sprite_height // 2
            shift = half_sprite_height * self.shift

            if self.death and self.health_point != -1:
                sprite_object = self.dead_animation()
                shift = half_sprite_height * self.shift
                sprite_height = int(sprite_height / 1.3)
            elif self.action_trigger:
                sprite_object = self.npc_in_action()
            else:
                self.object = self.visible_sprite()
                sprite_object = self.sprite_animation()

            # sprite scale and pos
            sprite_pos = (self.current_ray * SCALE - half_sprite_width, HALF_HEIGHT - half_sprite_height + shift)
            sprite = pygame.transform.scale(sprite_object, (sprite_width, sprite_height))
            return self.distance_to_sprite, sprite, sprite_pos
        else:
            return False, False, False

    def sprite_animation(self):
        if self.animation and self.distance_to_sprite < self.animation_dist:
            sprite_object = self.animation[0]
            if self.animation_count < self.animation_speed:
                self.animation_count += 1
            else:
                self.animation.rotate(-1)
                self.animation_count = 0
            return sprite_object
        return self.object

    def npc_in_action(self):
        if self.action_length == 0:
            self.action_length = len(self.param['animation'])
        sprite_object = self.action_animation[0]
        if self.animation_count < self.animation_speed:
            self.animation_count += 1
        else:
            self.action_animation.rotate(-1)
            self.action_length -= 1
            self.animation_count = 0
        return sprite_object

    def visible_sprite(self):
        if self.viewing_angles:
            if self.theta < 0:
                self.theta += DOUBLE_PI
            self.theta = 360 - int(math.degrees(self.theta))

            for angles in self.sprite_angles:
                if self.theta in angles:
                    return self.sprite_positions[angles]
        return self.object

    def dead_animation(self):
        if len(self.death_animation):
            if self.dead_animation_count < self.animation_speed:
                self.dead_sprite = self.death_animation[0]
                self.dead_animation_count += 1
            else:
                self.dead_sprite = self.death_animation.popleft()
                self.dead_animation_count = 0
        return self.dead_sprite

    def update_pos(self, pos: tuple[int, int]) -> None:
        self.pos = self.x, self.y = pos
        self.rect = pygame.Rect(*self.pos, self.side, self.side)

    def update_angle(self, angle: int) -> None:
        self.angle = angle
        if self.viewing_angles:
            self.sprite_angles = list(map(frozenset, get_sprite_angles(self.angle)))
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.objects)}
