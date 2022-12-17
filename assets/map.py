from settings import *

from numba.core import types
from numba.typed import Dict
from numba import int32

_ = False
matrix_map = [
    [1, 2, 4, 2, 1, 4, 1, 5, 1, 2, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 1, 2, 3, 1, _, 1, _, 1, 1, _, _, _, 1],
    [1, _, 4, _, _, _, _, _, _, 2, _, _, _, _, 1],
    [1, _, 2, _, _, 1, _, _, _, 1, _, _, 2, _, 1],
    [1, _, 1, _, 1, 2, _, _, _, _, _, _, _, _, 3],
    [1, _, _, _, _, _, _, _, _, _, _, _, 1, _, 2],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [4, _, _, _, _, _, _, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [3, _, 1, _, 1, _, 1, _, 1, _, 1, _, 1, _, 2],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 3, 1, 2, 5, 4, 1]
]

WORLD_WIDTH, WORLD_HEIGHT = len(matrix_map[0]) * TILE, len(matrix_map) * TILE
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char: world_map[(i * TILE, j * TILE)] = char
