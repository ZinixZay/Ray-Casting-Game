import pygame

from assets.map import world_map
from settings import *


def mapping(a: float, b: float) -> tuple:
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(player, textures, shadow: bool = True) -> list:
    walls = list()
    ox, oy = player.pos
    xm, ym = mapping(ox, oy)
    texture_v, texture_h = 1, 1
    cur_angle = player.angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * TILE

        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        # projection
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % TILE
        depth *= math.cos(player.angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(PROJ_COEFF / depth), 2 * HEIGHT)

        wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)

        if shadow:
            shadow = pygame.Surface((SCALE, proj_height), pygame.SRCALPHA)
            shadow.fill((0, 0, 0, min(depth / TILE * 20, 200)))
            wall_column.blit(shadow, (0, 0))

        walls.append((depth, wall_column, wall_pos))
        cur_angle += DELTA_ANGLE

    return walls
