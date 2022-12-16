import pygame

from entities.main_player import MainPlayer
from settings import *
from utils.drawing import Drawing
from utils.ray_casting import ray_casting


class RayCastingGame:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.player = MainPlayer(speed=4)
        self.drawing = Drawing(self.screen)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.player.movement()
            self.screen.fill(BLACK)
            walls = ray_casting(self.player, self.drawing.textures)

            self.drawing.draw_floor_sky(self.player.angle)
            self.drawing.draw_world_objects(walls)
            self.drawing.draw_fps(str(self.clock.get_fps()))

            pygame.display.flip()
            self.clock.tick()


if __name__ == '__main__':
    game = RayCastingGame()
    game.run()
