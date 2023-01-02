from settings import *
from numba import njit, float32, int32


@njit(float32(float32), fastmath=True, cache=True)
def get_sky_offset(angle):
    return -40 / 3 * math.degrees(angle)


@njit(int32(int32), fastmath=True, cache=True)
def normalize_angle(angle):
    return angle + math.ceil(-angle / 360) * 360


@njit(fastmath=True)
def get_sprite_angles(angle):
    result = list()
    for i in range(8):
        theta = normalize_angle(angle + 45 * i)
        result.append(list(map(normalize_angle, list(range(theta-22, theta+23)))))
    return result


@njit(fastmath=True, cache=True)
def get_left_top_coord_texture(offset, proj_height):
    if proj_height > HEIGHT:
        coeff = proj_height / HEIGHT
        texture_height = TEXTURE_HEIGHT / coeff
        return offset * TEXTURE_SCALE, HALF_TEXTURE_HEIGHT - texture_height // 2, TEXTURE_SCALE, texture_height
    return offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT
