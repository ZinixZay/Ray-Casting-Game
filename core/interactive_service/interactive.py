import math
from random import random

import pygame
from numba import njit

from core.entity_service.entity_service import EntityService
from core.sound_service.sound_service import SoundService
from core.utils.utils import mapping
from entities.main_player.main_player import MainPlayer
from settings import TILE
from statuses.status_entities import STATUS_ENTITIES


@njit(fastmath=True, cache=True)
def ray_casting_npc_player(npc_x, npc_y, world_map, player_pos):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    delta_x, delta_y = ox - npc_x, oy - npc_y
    cur_angle = math.atan2(delta_y, delta_x) + math.pi

    sin_a = math.sin(cur_angle)
    cos_a = math.cos(cur_angle)
    sin_a = sin_a if sin_a else 0.000001
    cos_a = cos_a if cos_a else 0.000001

    x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
    for i in range(0, int(abs(delta_x)) // TILE):
        depth_v = (x - ox) / cos_a
        yv = oy + depth_v * sin_a
        tile_v = mapping(x + dx, yv)
        if tile_v in world_map:
            return False
        x += dx * TILE

    y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
    for i in range(0, int(abs(delta_y)) // TILE):
        depth_h = (y - oy) / sin_a
        xh = ox + depth_h * cos_a
        tile_h = mapping(xh, y + dy)
        if tile_h in world_map:
            return False
        y += dy * TILE
    return True


class Interactive:
    def __init__(self, player: MainPlayer, entity_service: EntityService, sound_service: SoundService):
        self.player = player
        self.entity_service = entity_service
        self.sound_service = sound_service

    def shot(self):
        if self.player.shot:
            self.sound_service.shot()
            for obj in sorted(self.entity_service.entity_vulnerable, key=lambda obj: obj.distance(self.player)):
                if obj.is_on_fire(self.player)[1]:
                    obj.set_damage(self.player.weapon.damage)
                    break

    def npc_action(self, world_map):
        for obj in self.entity_service.entity_packs:
            if pygame.Rect.colliderect(self.player.rect, obj.rect):
                if obj.type == STATUS_ENTITIES.HEALTH_PACK and not obj.death:
                    self.player.heal(20)
                    obj.death = True
                if obj.type == STATUS_ENTITIES.BULLET_PACK and not obj.death:
                    self.sound_service.get_item_sound()
                    self.player.weapon.numbers_bullets += 10
                    obj.death = True
        for obj in self.entity_service.entity_vulnerable:
            if obj.type == STATUS_ENTITIES.NPC and not obj.death:
                if ray_casting_npc_player(obj.x, obj.y, world_map, self.player.pos):
                    obj.action_trigger = abs(obj.distance(self.player)) <= obj.action_dist
                    if abs(obj.distance(self.player)) <= obj.animation_dist and not obj.action_trigger:
                        self.npc_movement(obj)
                    elif obj.action_trigger and obj.action_length == 0:
                        if random() < obj.chance:
                            self.sound_service.sound_hit()
                            self.player.damage(obj.damage)

    def npc_movement(self, obj):
        if abs(obj.distance(self.player)) >= obj.action_dist:
            dx, dy = obj.x - self.player.pos[0], obj.y - self.player.pos[1]
            obj.update_pos((obj.x + obj.speed if dx < 0 else obj.x - obj.speed,
                            obj.y + obj.speed if dy < 0 else obj.y - obj.speed))
            obj.update_angle(math.degrees(math.atan2(dx, dy))-90)

