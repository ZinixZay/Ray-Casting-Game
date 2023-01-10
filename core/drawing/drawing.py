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

    def draw_world_objects(self, world_objects: list) -> None:
        for obj in filter(lambda el: el[0], sorted(world_objects, key=lambda n: n[0], reverse=True)):
            _, object_surface, object_pos = obj
            self.screen.blit(object_surface, object_pos)

    def draw_interface(self, player: MainPlayer, mini_map: set, fps='none') -> None:
        player.weapon.draw(self.screen)
        self.screen.blit(self.textures_interface['interface'], (MARGIN, HEIGHT-220-MARGIN))
        self.screen.blit(player.weapon.miniature, (225, HEIGHT-175))
        self.draw_weapon_info(player.weapon.name, player.weapon.get_bullet_str)
        self.draw_points(player.health_points, player.armor_points)
        self.draw_gameinfo([f'FPS: {fps}', f'Pos: {int(player.x//TILE)} {int(player.y//TILE)}'])
        self.draw_minimap(player, mini_map)

    def draw_weapon_info(self, weapon_name, bullet_number) -> None:
        weapon_name_text = self.font_hp.render(f'Weapon: {weapon_name}', 0, WHITE)
        bullets_text = self.font_bullet.render(bullet_number, 0, WHITE)

        self.screen.blit(self.textures_interface['bullet'], WEAPON_BULLET_POS)
        self.screen.blit(weapon_name_text, WEAPON_NAME_TEXT_POS)
        self.screen.blit(bullets_text, WEAPON_BULLET_NUMBER_POS)

    def draw_points(self, health_points, armor_points) -> None:
        hp_text = self.font_hp.render(f'Health: {health_points}/100', 0, WHITE)
        armor_text = self.font_hp.render(f'Armor: {armor_points}/100', 0, WHITE)

        self.screen.blit(hp_text, HEALTH_POINTS_TEXT_POS)
        self.screen.blit(self.textures_interface['points_background']
                         .subsurface(0, 0, 8 * math.ceil(health_points / 4), 15), HEALTH_POINTS_POS)
        self.screen.blit(self.textures_interface['points'], HEALTH_POINTS_POS)

        self.screen.blit(armor_text, ARMOR_POINTS_TEXT_POS)
        self.screen.blit(self.textures_interface['points_background']
                         .subsurface(0, 0, 8 * math.ceil(armor_points / 4), 15), ARMOR_POINTS_POS)
        self.screen.blit(self.textures_interface['points'], ARMOR_POINTS_POS)

    def draw_gameinfo(self, information: list) -> None:
        self.screen_gameinfo.fill(EMPTY_COLOR)
        for ind, text in enumerate(information):
            render = self.font_fps.render(text, 0, WHITE)
            self.screen_gameinfo.blit(render, (240 - 40*ind, 20 + 40*ind))
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
