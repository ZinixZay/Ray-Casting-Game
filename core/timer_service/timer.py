import datetime
import pygame


class Timer:
    def __init__(self) -> None:
        self.time = pygame.time
        self.start_sec = 0
        self.end_sec = None

    @property
    def time_pars(self) -> str:
        if self.end_sec:
            m = self.end_sec - self.start_sec
            return datetime.datetime(1, 1, 1, minute=int(
                (m / (1000 * 60)) % 60), second=int((m / 1000) % 60)).strftime('%M:%S')
        m = self.time.get_ticks() - self.start_sec
        return datetime.datetime(1, 1, 1, minute=int(
            (m / (1000 * 60)) % 60), second=int((m / 1000) % 60)).strftime('%M:%S')

    def start_time(self) -> None:
        self.start_sec = self.time.get_ticks()
        self.end_sec = None

    def stop_time(self) -> None:
        self.end_sec = self.time.get_ticks()
