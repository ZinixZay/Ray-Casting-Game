import pygame
from settings import *
from utils.ray_casting import ray_casting
from paths import *


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.textures = {
            1: pygame.image.load(IMAGES_PATH+'\\walls\\wall1.png').convert(),
            2: pygame.image.load(IMAGES_PATH + '\\walls\\wall2.png').convert(),
            3: pygame.image.load(IMAGES_PATH + '\\walls\\wall3.png').convert(),
            4: pygame.image.load(IMAGES_PATH + '\\walls\\wall4.png').convert(),
            5: pygame.image.load(IMAGES_PATH + '\\walls\\wall5.png').convert(),
            'S': pygame.image.load(IMAGES_PATH + '\\sky\\sky1.png').convert(),
        }

    def draw_floor_sky(self, angle: float) -> None:
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.screen.blit(self.textures['S'], (sky_offset, 0))
        self.screen.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.screen.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.screen, DARK_GRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def draw_world_objects(self, world_objects: list) -> None:
        for obj in filter(lambda el: el[0], sorted(world_objects, key=lambda n: n[0], reverse=True)):
            _, object_surface, object_pos = obj
            self.screen.blit(object_surface, object_pos)
