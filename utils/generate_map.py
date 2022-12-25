import numpy as np
import random
from utils.generate_rate_config import *


class MapGenerator:
    def __init__(self, width: int, height: int) -> None:
        self.width, self.height = width, height
        self.map = None
        self.space = list()
        self.hero_spawn = None

    def generate(self):
        new_map = np.zeros((self.height, self.width), dtype=np.int32)
        for row in range(self.height):
            for column in range(self.width):

                if row == 0 or row == (self.height - 1):
                    new_map[row] = [self.__generate_wall() for _ in range(self.width)]
                    break

                if column == 0 or column == (self.width - 1):
                    new_map[row][column] = self.__generate_wall()
                    continue

                new_map[row][column] = self.__generate_cell(row, column, new_map)

        self.map = new_map
        self.__destroy_no_ways()
        row, col = random.choice(self.space)
        new_map[row][col] = 5
        self.space.remove((row, col))
        self.hero_spawn = (row, col)

    @staticmethod
    def __generate_wall() -> int:
        for potential_wall, chance in generate_rate.items():
            return 2 if chance >= random.randint(0, 100) else 1

    @staticmethod
    def __get_neighbours(row, col) -> list:
        return [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]

    def __generate_cell(self, row, col, field):
        walls_near = 0
        wall_chance = intensivity
        for cell in self.__get_neighbours(row, col):
            if field[cell[0]][cell[1]] != 0:
                walls_near += 1
        match walls_near:
            case 0:
                rang = 100
            case 1:
                rang = 50
            case 2:
                rang = 50
            case 3:
                rang = 100
            case 4:
                rang = 0
        if wall_chance >= random.randint(0, rang):
            return self.__generate_wall()
        else:
            self.space.append((row, col))
            return 0

    def __destroy_no_ways(self):
        for row in range(self.height):
            for col in range(self.width):
                if row == 0 or col == 0 or row == self.height - 1 or col == self.width - 1:
                    continue
                walls_near = 0
                for cell in self.__get_neighbours(row, col):
                    if self.map[cell[0]][cell[1]] != 0:
                        walls_near += 1
                match walls_near:
                    case 0:
                        self.map[row][col] = 0
                    case 4:
                        self.map[row][col] = 1
                    case 3:
                        self.map[row][col] = 1


