import sys

import pygame

from components.menu_pause.menu_pause import MenuPause
from components.menu_start.menu_start import MenuStart
from core.interactive_service.interactive import Interactive
from core.status_game import STATUS_GAME
from entities.weapon.weapon import Weapon
from settings import *
from core.entity_service.entity_service import EntityService
from core.map_service.map_service import MapService
from core.drawing.drawing import Drawing
from core.ray_casting_service.ray_casting import ray_casting_walls_textured
from core.sound_service.sound_service import SoundService
from core.data_service.data_service import DataService
from entities.main_player.main_player import MainPlayer


class RayCastingGame:
    def __init__(self):
        pygame.init()
        icon = pygame.image.load(IMAGES_PATH+'\\icon\\icon.png')
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode(SIZE_SCREEN)

        self.data_service = DataService()

        self.sound_service = SoundService()
        self.sound_service.sound_menu()

        self.drawing = Drawing(self.screen)
        self.clock = pygame.time.Clock()
        pygame.event.set_grab(1)

        self.game_status = STATUS_GAME.MENU_START
        self.start_menu = MenuStart(self.drawing.textures_interface['button'],
                                    self.drawing.textures_interface['active_button'],
                                    self.drawing.textures_interface['background'])
        self.start_pause = MenuPause(self.drawing.textures_interface['button'],
                                     self.drawing.textures_interface['active_button'],
                                     self.drawing.textures_interface['background'])

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and self.game_status == STATUS_GAME.GAME_PROCESS:
                    self.game_status = STATUS_GAME.MENU_PAUSE

            if self.game_status == STATUS_GAME.MENU_START:
                self.start_menu_logic()
            elif self.game_status == STATUS_GAME.GAME_PROCESS or self.game_status == STATUS_GAME.GAME_PROCESS_RANDOM:
                self.game_process()
            elif self.game_status == STATUS_GAME.MENU_PAUSE:
                self.pause_menu_logic()

    def start_menu_logic(self):
        pygame.mouse.set_visible(True)
        self.start_menu.draw(self.screen)
        status = self.start_menu.get_status()
        if status:
            if status == STATUS_GAME.EXIT:
                pygame.quit()
                sys.exit()
            elif status == STATUS_GAME.GAME_PROCESS:
                self.game_status = STATUS_GAME.GAME_PROCESS
                self.start_game(1)
            elif status == STATUS_GAME.GAME_PROCESS_RANDOM:
                self.game_status = STATUS_GAME.GAME_PROCESS_RANDOM
                self.start_game_random()
        pygame.display.flip()
        self.clock.tick(FPS)

    def pause_menu_logic(self):
        pygame.mouse.set_visible(True)
        self.sound_service.sound_pause()
        self.start_pause.draw(self.screen)
        status = self.start_pause.get_status()
        if status:
            if status == STATUS_GAME.EXIT:
                pygame.quit()
                sys.exit()
            elif status == STATUS_GAME.GAME_PROCESS:
                self.game_status = STATUS_GAME.GAME_PROCESS
                self.sound_service.sound_unpause()
                pygame.mouse.set_visible(False)
                self.game_process()
            elif status == STATUS_GAME.MENU_START:
                self.sound_service.sound_menu()
                self.game_status = STATUS_GAME.MENU_START
        pygame.display.flip()
        self.clock.tick(FPS)

    def start_game_random(self):
        self.sound_service.sound_start()
        self.sound_service.sound_game()
        pygame.mouse.set_visible(False)
        self.map_service = MapService()
        self.map_service.generate_map()

        self.entity_service = EntityService(self.map_service.entities)

        self.weapon = Weapon(WEAPONS_PARAM['test_weapon'])
        self.player = MainPlayer(self.map_service.start_player_pos, self.weapon, angle=0, speed=8)
        self.player.update_collision_objs(self.map_service.collisions
                                          + [i.rect for i in self.entity_service.entities if i.blocked])

    def start_game(self, map_lvl=1):
        self.sound_service.sound_start()
        self.sound_service.sound_game()
        pygame.mouse.set_visible(False)
        self.map_lvl = map_lvl
        self.map_service = MapService()
        self.map_service.load_map(self.map_lvl)

        self.entity_service = EntityService(self.map_service.entities)
        self.interactive_service = Interactive(self.entity_service)

        self.weapon = Weapon(WEAPONS_PARAM['test_weapon'])
        self.player = MainPlayer(self.map_service.start_player_pos, self.weapon, angle=0, speed=8)
        self.player.update_collision_objs(self.map_service.collisions
                                          + [i.rect for i in self.entity_service.entities if i.blocked])

    def game_process(self):
        self.screen.fill(BLACK)
        if self.player.rect.collidepoint(self.map_service.end_point):
            self.start_game(self.map_lvl+1)
        self.player.movement()
        self.interactive_service.shot(self.player)
        self.sound_service.sound_steps(self.player.is_moving())
        self.drawing.draw_floor_sky(self.player.angle)
        self.drawing.draw_world_objects(
            ray_casting_walls_textured(self.player, self.drawing.textures, self.map_service.walls)
            + [obj.object_locate(self.player) for obj in self.entity_service.entities]
        )
        self.drawing.draw_interface(self.player, self.map_service.mini_map, round(self.clock.get_fps()))
        pygame.display.flip()
        self.clock.tick(FPS)


if __name__ == '__main__':
    game = RayCastingGame()
    game.run()
