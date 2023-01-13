import pygame


class Interactive:
    def __init__(self, entity_service):
        self.entity_service = entity_service

    def shot(self, player):
        if player.shot: print(player.shot)
