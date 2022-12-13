import pygame
from settings import *


class MainPlayer:
    def __init__(self, pos=(HALF_WIDTH, HALF_HEIGHT), angle=0, speed=2):
        self.x, self.y = pos
        self.angle = angle
        self.speed = speed
        self.sensitivity = 0.004

    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
        self.keys_control()
        self.mouse_control()

    def keys_control(self):
        sin_a, cos_a = math.sin(self.angle), math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()

        if keys[pygame.K_w]:
            self.x += self.speed * cos_a
            self.y += self.speed * sin_a
        if keys[pygame.K_s]:
            self.x += -self.speed * cos_a
            self.y += -self.speed * sin_a
        if keys[pygame.K_a]:
            self.x += self.speed * sin_a
            self.y += -self.speed * cos_a
        if keys[pygame.K_d]:
            self.x += -self.speed * sin_a
            self.y += self.speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivity
