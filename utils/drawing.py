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
        }

    def background(self):
        pygame.draw.rect(self.screen, DARK_GRAY, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.screen, BLACK, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.screen, player_pos, player_angle, self.textures)
