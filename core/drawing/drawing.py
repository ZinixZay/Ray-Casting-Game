import pygame
from core.utils.utils import get_sky_offset
from entities.main_player.main_player import MainPlayer
from paths import FONT_PATH
from settings import *


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.screen_gameinfo = pygame.Surface(GAMEINFO_SIZE, pygame.SRCALPHA)
        self.screen_minimap = pygame.Surface(MINIMAP_SIZE, pygame.SRCALPHA)
        self.minimap_walls_screen = pygame.Surface(MINIMAP_SIZE, pygame.SRCALPHA)
        self.font_fps = pygame.font.Font(FONT_PATH+'Fifaks10Dev1.ttf', 34)
        self.font_hp = pygame.font.Font(FONT_PATH+'Fifaks10Dev1.ttf', 20)
        self.font_bullet = pygame.font.Font(FONT_PATH+'Fifaks10Dev1.ttf', 26)
        self.textures = dict()
        self.textures_interface = dict()
        self.load_textures()
        self.load_textures_interface()

    def load_textures(self) -> None:
        for key in TEXTURES:
            self.textures[key] = pygame.image.load(TEXTURES[key]).convert()

    def load_textures_interface(self) -> None:
        for key in TEXTURES_INTERFACE:
            self.textures_interface[key] = pygame.image.load(TEXTURES_INTERFACE[key]).convert_alpha()

    def draw_floor_sky(self, angle: float) -> None:
        sky_offset = get_sky_offset(angle)
        self.screen.blit(self.textures['S'], (sky_offset, 0))
        self.screen.blit(self.textures['S'], (sky_offset+4800, 0))
        self.screen.blit(self.textures['F'], (0, HALF_HEIGHT))
        # pygame.draw.rect(self.screen, DARK_GRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def draw_world_objects(self, world_objects: list) -> None:
        for obj in filter(lambda el: el[0], sorted(world_objects, key=lambda n: n[0], reverse=True)):
            _, object_surface, object_pos = obj
            self.screen.blit(object_surface, object_pos)

    def draw_interface(self, player: MainPlayer, mini_map, hp, armor, fps='none') -> None:
        self.screen.blit(self.textures_interface['interface'], (MARGIN, HEIGHT-220-MARGIN))
        self.screen.blit(self.textures_interface['bullet'], (MARGIN+HALF_WIDTH+76, HEIGHT - 95 - MARGIN))
        gun_text = self.font_hp.render(f'Weapon: ZEDGUN', 0, WHITE)
        self.screen.blit(gun_text, (MARGIN + HALF_WIDTH + 56, HEIGHT - 120 - MARGIN))
        bullets_text = self.font_bullet.render(f'10/20', 0, WHITE)
        self.screen.blit(bullets_text, (MARGIN+HALF_WIDTH+104, HEIGHT - 88 - MARGIN))
        self.draw_points(hp, armor)
        self.draw_gameinfo(fps)
        self.draw_minimap(player, mini_map)

    def draw_points(self, hp, armor) -> None:
        hp_text = self.font_hp.render(f'Health: {hp}/100', 0, WHITE)
        self.screen.blit(hp_text, HEALTH_POINTS_TEXT_POS)
        self.screen.blit(self.textures_interface['points_background'].subsurface(0, 0, 8 * math.ceil(hp / 4), 15),
                         HEALTH_POINTS_POS)
        self.screen.blit(self.textures_interface['points'], HEALTH_POINTS_POS)

        armor_text = self.font_hp.render(f'Armor: {armor}/100', 0, WHITE)
        self.screen.blit(armor_text, (MARGIN + 445, HEIGHT - 65 - MARGIN))
        self.screen.blit(self.textures_interface['points_background'].subsurface(0, 0, 8 * math.ceil(armor / 4), 15),
                         (MARGIN + 445, HEIGHT - 45 - MARGIN))
        self.screen.blit(self.textures_interface['points'], (MARGIN + 445, HEIGHT - 45 - MARGIN))

    def draw_gameinfo(self, fps='none'):
        self.screen_gameinfo.fill(EMPTY_COLOR)
        fps_text = self.font_fps.render(f'FPS: {fps}', 0, WHITE)
        test1_text = self.font_fps.render('TEST TEXT INFO', 0, WHITE)
        test2_text = self.font_fps.render('ZED DUCK', 0, WHITE)
        self.screen_gameinfo.blit(fps_text, (240, 20))
        self.screen_gameinfo.blit(test2_text, (200, 60))
        self.screen_gameinfo.blit(test1_text, (160, 100))
        self.screen.blit(self.screen_gameinfo, GAMEINFO_POS)

    def draw_minimap(self, player: MainPlayer, minimap) -> None:
        self.screen_minimap.blit(self.textures_interface['minimap_background'], (0, 0))
        self.minimap_walls_screen.fill(EMPTY_COLOR)

        dx, dy = player.x // MINIMAP_SCALE, player.y // MINIMAP_SCALE

        player_point = pygame.transform.rotate(self.textures_interface['player_point'], 360 - math.degrees(player.angle))
        coord_player_point = player_point.get_rect().width // 2
        self.screen_minimap.blit(player_point,
                                 (HALF_MINIMAP_WIDTH - coord_player_point, HALF_MINIMAP_HEIGHT - coord_player_point))

        camera_rect = pygame.Rect(dx - HALF_MINIMAP_WIDTH, dy - HALF_MINIMAP_HEIGHT,
                                  MINIMAP_WIDTH, MINIMAP_HEIGHT)
        diffx, diffy = HALF_MINIMAP_WIDTH - dx, HALF_MINIMAP_HEIGHT - dy

        for wall in minimap:
            wall_rect = pygame.Rect(wall[0], wall[1], MINIMAP_TILE, MINIMAP_TILE)
            if camera_rect.colliderect(wall_rect):
                pygame.draw.rect(self.minimap_walls_screen, MAP_WALLS_COLOR,
                                 pygame.Rect(wall_rect.x + diffx, wall_rect.y + diffy, MINIMAP_TILE, MINIMAP_TILE))

        self.screen_minimap.blit(self.minimap_walls_screen, (0, 0))
        self.screen.blit(self.screen_minimap, MINIMAP_POS)
