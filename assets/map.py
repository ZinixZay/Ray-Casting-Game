from settings import *

_ = False
matrix_map = [
    [1, 1, 1, 2, 1, 4, 1, 5, 1, 2, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 3, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, 4, _, _, _, _, _, _, 1],
    [1, _, 1, 2, 2, _, 3, _, 4, _, 5, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

world_map = {}
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char: world_map[(i * TILE, j * TILE)] = char
