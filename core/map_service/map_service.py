from core.map_generator.map_generator import MapGenerator
from numba.core import types
from numba.typed import Dict
from numba import int32
from core.map_service.config import *
from paths import *
import pygame
import json


class MapService:
    def __init__(self) -> None:
        self.map_generator = MapGenerator(*WORLD_SIZE)
        self.matrix_map = list()
        self.collisions = list()
        self.walls = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
        self.start_player_pos = None

    def generate_map(self) -> None:
        self.map_generator.generate()
        self.matrix_map = self.map_generator.map
        self.reset_param()

    def load_map(self, number_map: int) -> None:
        with open(MAPS_PATH+f'map{number_map}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.matrix_map = data["matrix_map"]
        self.reset_param()

    def reset_param(self):
        self.walls = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
        self.collisions = list()
        for j, row in enumerate(self.matrix_map):
            for i, char in enumerate(row):
                if char:
                    self.collisions.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
                    self.walls[(i * TILE, j * TILE)] = char
