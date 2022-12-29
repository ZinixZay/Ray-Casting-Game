import pygame

from core.map_service.map_service import MapService
from entities.main_player import MainPlayer
from settings import *
from core.drawing.drawing import Drawing
from core.ray_casting_service.ray_casting import ray_casting_walls_textured


class RayCastingGame:
    def __init__(self) -> None:
        pygame.init()
        pygame.mouse.set_visible(False)

        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        self.screen_minimap = pygame.Surface((300, 200))
        self.drawing = Drawing(self.screen, self.screen_minimap)

        self.clock = pygame.time.Clock()
        pygame.event.set_grab(1)

        self.map_service = MapService()
        self.map_service.load_map(1)

        self.player = MainPlayer((HALF_WIDTH, HALF_HEIGHT), speed=10)
        self.player.update_collision_objs(self.map_service.collisions)

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
            self.drawing.draw_minimap(self.player, self.map_service.mini_map)
            self.drawing.draw_fps(str(self.clock.get_fps()))

            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = RayCastingGame()
    game.run()
