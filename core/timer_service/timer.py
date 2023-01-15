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
            timer_process = threading.Thread(target=self.time_proc)
            timer_process.start()

    def __reboot(self):
        self.end_time = None
        self.cur_time = None
        self.available = True

    def time_proc(self):
        while self.end_time > round(time.time()):
            self.cur_time = self.end_time - round(time.time())
        self.__reboot()

    def get_parsed_time(self) -> tuple:
        minutes = self.cur_time // 60
        seconds = self.cur_time % 60
        return minutes, seconds
