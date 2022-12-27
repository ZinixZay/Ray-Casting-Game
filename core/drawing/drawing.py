import pygame
from core.utils.utils import get_sky_offset
from core.drawing.config import *


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = dict()
        self.load_textures()

    def load_textures(self) -> None:
        for key in TEXTURES:
            self.textures[key] = pygame.image.load(TEXTURES[key]).convert()

    def draw_floor_sky(self, angle: float) -> None:
        sky_offset = get_sky_offset(angle)
        self.screen.blit(self.textures['S'], (sky_offset, 0))
        self.screen.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.screen.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.screen, DARK_GRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def draw_world_objects(self, world_objects: list) -> None:
        for obj in filter(lambda el: el[0], sorted(world_objects, key=lambda n: n[0], reverse=True)):
            _, object_surface, object_pos = obj
            self.screen.blit(object_surface, object_pos)

    def draw_fps(self, fps_value):
        render = self.font.render(fps_value, 0, WHITE)
        self.screen.blit(render, (WIDTH - 65, 5))
