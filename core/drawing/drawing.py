from pprint import pprint

import pygame
from core.utils.utils import get_sky_offset
from core.drawing.config import *


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(FONT_PATH+'Fifaks10Dev1.ttf', 36)
        self.textures = dict()
        self.interface_texture = pygame.image.load(IMAGES_PATH+'interface\\interface_1.png').convert()
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

    def draw_fps(self, fps_value):
        render = self.font.render(fps_value, 0, WHITE)
        self.screen.blit(render, (WIDTH - 65, 5))

    # def draw_minimap(self, player, mini_map):
    #     self.screen_minimap.fill(BLACK)
    #     map_x, map_y = player.x // MINIMAP_SCALE, player.y // MINIMAP_SCALE
    #     pygame.draw.circle(self.screen_minimap, RED, (int(map_x), int(map_y)), 4)
    #     for x, y in mini_map:
    #         pygame.draw.rect(self.screen_minimap, BLUE, (x, y, MINIMAP_TILE, MINIMAP_TILE))
    #     pygame.draw.line(self.screen_minimap, RED, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
    #                                                                        map_y + 12 * math.sin(player.angle)), 2)
    #     self.screen_interface.blit(self.screen_minimap, (0, 0))
    #
    # def draw_interface(self, player, mini_map):
    #     self.screen_interface.fill((24, 27, 33))
    #     self.draw_minimap(player, mini_map)
    #     self.screen_info.fill((0, 0, 255))
    #     self.screen_interface.blit(self.screen_info, (880, 0))
    #
    #     self.screen.blit(self.screen_interface, (10, HEIGHT-210))
