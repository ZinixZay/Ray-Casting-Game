import pygame

from assets.map import world_map, collision_walls
from entities.main_player import MainPlayer
from settings import *
from utils.drawing import Drawing
from utils.ray_casting import ray_casting_walls_textured


class RayCastingGame:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.player = MainPlayer((HALF_WIDTH, HALF_HEIGHT), speed=6)
        self.player.update_collision_objs(collision_walls)
        self.drawing = Drawing(self.screen)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.player.movement()
            self.screen.fill(BLACK)

            self.drawing.draw_floor_sky(self.player.angle)
            self.drawing.draw_world_objects(ray_casting_walls_textured(self.player, self.drawing.textures, world_map))
            self.drawing.draw_fps(str(self.clock.get_fps()))

            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = RayCastingGame()
    game.run()
