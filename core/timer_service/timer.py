import datetime

import pygame


class Timer:
    def __init__(self):
        self.time = pygame.time
        self.start_sec = 0
        self.end_sec = None

    @property
    def time_pars(self):
        if self.end_sec:
            return datetime.datetime(1, 1, 1, second=(self.end_sec - self.start_sec)//1000).strftime('%M:%S')
        return datetime.datetime(1, 1, 1, second=(self.time.get_ticks() - self.start_sec)//1000).strftime('%M:%S')

    def start_time(self):
        self.start_sec = self.time.get_ticks()
        self.end_sec = None

    def stop_time(self):
        self.end_sec = self.time.get_ticks()
