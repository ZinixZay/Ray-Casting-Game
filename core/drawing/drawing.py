import pygame
from core.utils.utils import get_sky_offset
from paths import FONT_PATH, IMAGES_PATH
from settings import TEXTURES, DARK_GRAY, HALF_HEIGHT, WIDTH, WHITE, BLACK, MINIMAP_SCALE, RED, INTERFACE_COLOR, \
    MINIMAP_TILE, MINIMAP_POS, MINIMAP_SIZE, GAMEINFO_SIZE, GAMEINFO_POS, MAP_WALLS_COLOR, FPS_POS


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.screen_minimap = pygame.Surface(MINIMAP_SIZE)
        self.screen_gameinfo = pygame.Surface(GAMEINFO_SIZE)
        self.font_fps = pygame.font.Font(FONT_PATH+'Fifaks10Dev1.ttf', 26)
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

    def draw_interface(self, player, mini_map, fps='none'):
        self.draw_minimap(player, mini_map)
        self.draw_gameinfo(player, fps)

    def draw_minimap(self, player, mini_map):
        self.screen_minimap.fill(BLACK)
        map_x, map_y = player.x // MINIMAP_SCALE, player.y // MINIMAP_SCALE
        pygame.draw.circle(self.screen_minimap, RED, (int(map_x), int(map_y)), 4)
        for x, y in mini_map:
            pygame.draw.rect(self.screen_minimap, MAP_WALLS_COLOR, (x, y, MINIMAP_TILE, MINIMAP_TILE))
        self.screen.blit(self.screen_minimap, MINIMAP_POS)

    def draw_gameinfo(self, player, fps='none'):
        self.screen_gameinfo.fill(INTERFACE_COLOR)
        fps_text = self.font_fps.render(f'FPS: {fps}', 0, WHITE)
        self.screen_gameinfo.blit(fps_text, FPS_POS )
        self.screen.blit(self.screen_gameinfo, GAMEINFO_POS)
