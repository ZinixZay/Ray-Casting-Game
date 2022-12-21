# TODO: create a class for map generator
import numpy as np
import random
from generate_rate_config import *


class MapGenerator:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = None

    def generate(self):
        new_map = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for row in range(self.height):
            for column in range(self.width):

                if row == 0 or row == (self.height - 1):
                    new_map[row] = [self.__generate_wall() for _ in range(self.width)]
                    break

                if column == 0 or column == (self.width - 1):
                    new_map[row][column] = self.__generate_wall()
                    continue

                new_map[row][column] = self.__generate_cell(row, column, new_map)

        self.map = np.asarray(new_map)

    @staticmethod
    def __generate_wall() -> int:
        for potential_wall, chance in generate_rate.items():
            if chance >= random.randint(0, 100):
                return 2
            else:
                return 1

    def __generate_cell(self, row, col, field):
        c = 0
        wall_chance = intensivity
        neighbours = [[row + 1, col], [row, col + 1], [row - 1, col], [row, col - 1]]
        for cell in neighbours:
            if field[cell[0]][cell[1]] == 0:
                c += 1
        rang = 100 - c * 10
        if wall_chance >= random.randint(0, rang):
            return self.__generate_wall()
        else:
            return 0


gr = MapGenerator(10, 15)
gr.generate()
print(gr.map)


