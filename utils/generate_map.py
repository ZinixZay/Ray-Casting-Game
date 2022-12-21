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
        new_map = list()
        for row in range(self.height):
            new_row = []
            for column in range(self.width):

                if row == 0 or row == (self.height - 1):
                    new_map.append([self.__build_wall() for _ in range(self.width)])
                    break

                if column == 0 or column == (self.width - 1):
                    new_row.append(self.__build_wall())
                    continue

                new_row.append(0)

            else:
                new_map.append(new_row)
        self.map = np.asarray(new_map)

    @staticmethod
    def __build_wall() -> int:
        for potential_wall, chance in generate_rate.items():
            if chance >= random.randint(0, 100):
                return 2
            else:
                return 1


gr = MapGenerator(5, 20)
gr.generate()
print(gr.map)


