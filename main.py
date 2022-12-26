import pygame

from assets.map import MapService
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
        self.map_service = MapService()
        self.map_service.load_map_local('1')
        self.player = MainPlayer(self.map_service.start_player_pos, speed=6)
        self.player.update_collision_objs(self.map_service.collision_walls)
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
                ray_casting_walls_textured(self.player, self.drawing.textures, self.map_service.world_map)
            )
            self.drawing.draw_fps(str(self.clock.get_fps()))

            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = RayCastingGame()
    game.run()
