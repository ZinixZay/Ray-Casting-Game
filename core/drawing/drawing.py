import pygame
from core.utils.utils import get_sky_offset
from paths import FONT_PATH, IMAGES_PATH
from settings import *


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.screen_gameinfo = pygame.Surface((440, 217), pygame.SRCALPHA)
        self.font_fps = pygame.font.Font(FONT_PATH+'Fifaks10Dev1.ttf', 34)
        self.textures = dict()
        self.interface_texture = pygame.image.load(INTERFACE_TEXTURE).convert_alpha()
        self.load_textures()

    def load_textures(self) -> None:
        for key in TEXTURES:
            self.textures[key] = pygame.image.load(TEXTURES[key]).convert()

    def draw_floor_sky(self, angle: float) -> None:
        sky_offset = get_sky_offset(angle)
        self.screen.blit(self.textures['S'], (sky_offset, 0))
        self.screen.blit(self.textures['S'], (sky_offset+4800, 0))
        pygame.draw.rect(self.screen, DARK_GRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def draw_world_objects(self, world_objects: list) -> None:
        for obj in filter(lambda el: el[0], sorted(world_objects, key=lambda n: n[0], reverse=True)):
            _, object_surface, object_pos = obj
            self.screen.blit(object_surface, object_pos)

    def draw_interface(self, player, mini_map, fps='none'):
        self.screen_gameinfo.fill((0, 0, 0, 0))
        self.screen.blit(self.interface_texture, (MARGIN, HEIGHT-220-MARGIN))
        fps_text = self.font_fps.render(f'FPS: {fps}', 0, WHITE)
        test1_text = self.font_fps.render('TEST TEXT INFO', 0, WHITE)
        test2_text = self.font_fps.render('ZED DUCK', 0, WHITE)
        self.screen_gameinfo.blit(fps_text, (240, 20))
        self.screen_gameinfo.blit(test2_text, (200, 60))
        self.screen_gameinfo.blit(test1_text, (160, 100))
        self.screen.blit(self.screen_gameinfo, (WIDTH-MARGIN-440, HEIGHT-220-MARGIN))
