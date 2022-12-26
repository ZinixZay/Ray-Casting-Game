from settings import *
from numba.core import types
from numba.typed import Dict
from numba import int32
import pygame
import json


class MapService:
    def __init__(self):
        self.matrix_map = None
        self.start_player_pos = (4, 4)
        self.collision_walls = list()
        self.world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)

    def reset_values(self):
        self.matrix_map = None
        self.collision_walls = list()
        self.world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)

    @staticmethod
    def __convert_player_pos(pos: list[int, int]) -> tuple[int, int]:
        return pos[0] * TILE, pos[1] * TILE

    def set_data(self, data) -> None:
        self.reset_values()
        self.matrix_map = data['matrix_map']
        self.start_player_pos = self.__convert_player_pos(data['player']['start_pos'])
        for j, row in enumerate(self.matrix_map):
            for i, char in enumerate(row):
                if char:
                    self.collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
                    self.world_map[(i * TILE, j * TILE)] = char

    def load_map_local(self, number_map):
        file = open(f'assets/maps/map{number_map}.json')
        data = json.load(file)
        file.close()
        self.set_data(data)

