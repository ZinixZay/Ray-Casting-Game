import math
from random import random

import pygame
from numba import njit

from core.utils.utils import mapping, normalize_angle
from settings import TILE


@njit(fastmath=True, cache=True)
def ray_casting_npc_player(npc_x, npc_y, world_map, player_pos):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    delta_x, delta_y = ox - npc_x, oy - npc_y
    cur_angle = math.atan2(delta_y, delta_x)
    cur_angle += math.pi

    sin_a = math.sin(cur_angle)
    sin_a = sin_a if sin_a else 0.000001
    cos_a = math.cos(cur_angle)
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
    def __init__(self, entity_service):
        self.entity_service = entity_service

    def shot(self, player):
        if player.shot:
            for obj in sorted(self.entity_service.entity_vulnerable, key=lambda obj: obj.distance(player)):
                if obj.is_on_fire(player)[1]:
                    obj.health_point -= player.weapon.damage
                if obj.health_point <= 0:
                    obj.death = True

    def npc_action(self, player, world_map):
        for obj in self.entity_service.entity_vulnerable:
            if obj.type == 'npc' and not obj.death:
                if ray_casting_npc_player(obj.x, obj.y, world_map, player.pos):
                    obj.action_trigger = abs(obj.distance(player)) <= obj.action_dist
                    if not obj.action_trigger:
                        self.npc_move(player, obj)
                    elif obj.action_trigger and obj.action_length == 0:
                        if random() < obj.chance:
                            player.damage(obj.damage)



    def npc_move(self, player, obj):
        if abs(obj.distance(player)) >= obj.action_dist:
            dx, dy = obj.x - player.pos[0], obj.y - player.pos[1]
            obj.update_pos((obj.x + obj.speed if dx < 0 else obj.x - obj.speed,  obj.y + obj.speed if dy < 0 else obj.y - obj.speed))
            obj.update_angle(math.degrees(math.atan2(dx, dy))-90)

