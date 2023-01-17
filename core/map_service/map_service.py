import json
import pygame

from numba import int64
from numba.core import types
from numba.typed import Dict
from core.map_generator.map_generator import MapGenerator
from paths import MAPS_PATH
from settings import WORLD_SIZE, TILE, MINIMAP_TILE, HALF_TILE


class MapService:
    def __init__(self) -> None:
        self.map_generator = MapGenerator(*WORLD_SIZE)
        self.matrix_map = list()
        self.collisions = list()
        self.walls = Dict.empty(key_type=types.UniTuple(int64, 2), value_type=int64)
        self.start_player_pos = None
        self.player_angle = None
        self.entities = list()
        self.mini_map = set()

    def generate_map(self) -> None:
        self.map_generator.generate()
        self.matrix_map = self.map_generator.map
        self.start_player_pos = list(map(lambda coord: coord*TILE+HALF_TILE, self.map_generator.hero_spawn))
        self.player_angle = 0
        self.reset_param()

    def load_map(self, number_map: int) -> None:
        with open(MAPS_PATH+f'map{number_map}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.matrix_map = data["matrix_map"]
        self.start_player_pos = list(map(lambda coord: coord*TILE+HALF_TILE, data["player"]["start_pos"]))
        self.player_angle = data["player"]["angle"]
        self.entities = data["entities"]
        self.reset_param()

    def reset_param(self) -> None:
        self.walls = Dict.empty(key_type=types.UniTuple(int64, 2), value_type=int64)
        self.collisions.clear()
        self.mini_map.clear()
        for j, row in enumerate(self.matrix_map):
            for i, char in enumerate(row):
                if char and char != 100:
                    self.collisions.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
                    self.walls[(i * TILE, j * TILE)] = char
                    self.mini_map.add((i * MINIMAP_TILE, j * MINIMAP_TILE))
