from settings import *
from numba import njit, float32


@njit(float32(float32), fastmath=True, cache=True)
def get_sky_offset(angle):
    deg = math.degrees(angle)
    return -480 / 36 * deg


@njit(fastmath=True, cache=True)
def get_left_top_coord_texture(offset, proj_height):
    if proj_height > HEIGHT:
        coeff = proj_height / HEIGHT
        texture_height = TEXTURE_HEIGHT / coeff
        return offset * TEXTURE_SCALE, HALF_TEXTURE_HEIGHT - texture_height // 2, TEXTURE_SCALE, texture_height
    else:
        return offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT
