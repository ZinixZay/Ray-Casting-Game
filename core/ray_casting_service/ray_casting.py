import pygame
from settings import *
from numba import njit, prange
from core.utils.utils import get_left_top_coord_texture


@njit(fastmath=True, cache=True)
def mapping(a, b):
    return int(a // TILE) * TILE, int(b // TILE) * TILE


@njit(fastmath=True, cache=True)
def ray_casting(player_pos, player_angle, world_map):
    walls = list()
    ox, oy = player_pos
    texture_v, texture_h = 0, 0
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in prange(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = math.cos(cur_angle)
        cos_a = cos_a if cos_a else 0.000001

        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in prange(0, WORLD_WIDTH_TILE, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * TILE

        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in prange(0, WORLD_HEIGHT_TILE, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % TILE
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = int(PROJ_COEFF / depth) * 1.6

        walls.append((ray, depth, offset, proj_height, texture))
        cur_angle += DELTA_ANGLE
    return walls


def ray_casting_walls_textured(player, textures, world_map) -> list:
    walls = ray_casting(player.pos, player.angle, world_map)
    walls_textured = list()
    for casted_values in walls:
        ray, depth, offset, proj_height, texture = casted_values

        if proj_height > HEIGHT:
            wall_pos = (ray * SCALE, 0)
            scale_wall = (SCALE, HEIGHT)
        else:
            wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
            scale_wall = (SCALE, proj_height)

        wall_column = pygame.transform.scale(textures[texture if texture in textures.keys() else 0]
                                             .subsurface(*get_left_top_coord_texture(offset, proj_height)), scale_wall)
        if proj_height < HEIGHT * 1.4:
            shadow = pygame.Surface((SCALE, proj_height), pygame.SRCALPHA)
            shadow.fill((0, 0, 0, min(depth / TILE * 10, 200)))
            wall_column.blit(shadow, (0, 0))
        walls_textured.append((depth, wall_column, wall_pos))
    return walls_textured
