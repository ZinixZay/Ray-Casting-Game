import time
import threading


class Timer:
    def __init__(self):
        self.cur_time = None
        self.available = True
        self.start_time = None

    def set_timer(self):
        if self.available:
            self.available = False
            self.start_time = round(time.time())
            timer_process = threading.Thread(target=self.time_proc)
            timer_process.start()

    def __reboot(self):
        self.cur_time = None
        self.available = True
        self.start_time = None

    def time_proc(self):
        while not self.available:
            self.cur_time = round(time.time()) - self.start_time
        self.__reboot()

    def stop_timer(self):
        self.available = True

    def get_parsed_time(self) -> tuple:
        minutes = self.cur_time // 60
        seconds = self.cur_time % 60
        return minutes, seconds
