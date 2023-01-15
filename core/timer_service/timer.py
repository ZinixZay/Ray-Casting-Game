import time
import threading


class Timer:
    def __init__(self):
        self.end_time = None
        self.cur_time = None
        self.available = True

    def set_timer(self, seconds: int):
        if self.available:
            self.available = False
            self.end_time = round(time.time()) + seconds

    def __reboot(self):
        self.end_time = None
        self.cur_time = None
        self.available = True

    def time_proc(self):
        while self.end_time > round(time.time()):
            self.cur_time = self.end_time - round(time.time())
        self.__reboot()
