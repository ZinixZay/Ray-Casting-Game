import pygame

from core.map_service.map_service import MapService
from entities.main_player import MainPlayer
from settings import *
from core.drawing.drawing import Drawing
from core.ray_casting_service.ray_casting import ray_casting_walls_textured


class RayCastingGame:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.player = MainPlayer((HALF_WIDTH, HALF_HEIGHT), speed=6)
        self.map_service = MapService()
        self.map_service.generate_map()
        self.player.update_collision_objs(self.map_service.collisions)
        self.drawing = Drawing(self.screen)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.player.movement()
            self.screen.fill(BLACK)

            self.drawing.draw_floor_sky(self.player.angle)
            self.drawing.draw_world_objects(
                ray_casting_walls_textured(self.player, self.drawing.textures, self.map_service.walls)
            )
            self.drawing.draw_fps(str(self.clock.get_fps()))

            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = RayCastingGame()
    game.run()
