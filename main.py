import pygame

from entities.main_player import MainPlayer
from settings import *
from utils.drawing import Drawing

pygame.init()
screen = pygame.display.set_mode(SIZE_SCREEN)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
player = MainPlayer(speed=4)
drawing = Drawing(screen)


class RayCastingGame:
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            player.movement()
            screen.fill(BLACK)

            drawing.background()
            drawing.world(player.pos, player.angle)

            pygame.display.flip()
            clock.tick(FPS)


if __name__ == '__main__':
    game = RayCastingGame()
    game.run()
