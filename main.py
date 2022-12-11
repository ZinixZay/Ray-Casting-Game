import pygame
from settings import *

pygame.init()
screen = pygame.display.set_mode(SIZE_SCREEN)
clock = pygame.time.Clock()


class RayCastingGame:
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            screen.fill(BLACK)

            pygame.display.flip()
            clock.tick(FPS)


if __name__ == '__main__':
    game = RayCastingGame()
    game.run()
