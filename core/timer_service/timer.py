import time
import threading


class Timer:
    def __init__(self):
        self.end_time = None

    def set_timer(self, seconds: int):
        self.end_time = round(time.time()) + seconds

    def __reboot(self):
        self.end_time = None

    # def time_proc(self):
    #     while self.end_time > round(time.time()):

