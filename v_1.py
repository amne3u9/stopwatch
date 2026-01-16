import time


class Stopwatch:
    # общее время сессии за день
    def __init__(self):
        self.total_time_day = []
        self.running = False
        self.start_time = 0.0
        self.total_t = 0.0

    def start_t(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def stop_t(self):
        if self.running:
            self.total_t += (time.time() - self.start_time)
            self.running = False

    def reset_t(self):
        if self.running:
            self.total_t += (time.time() - self.start_time)
            # сохранить total_t в 'время' сессии за день
            self.total_time_day.append(self.total_t)
            # обнулить total_t
            self.total_t = 0.0
            self.running = False
        elif self.total_t > 0.0:
            # сохранить total_t в 'время' сессии за день
            self.total_time_day.append(self.total_t)
            self.total_t = 0.0

timer = Stopwatch()
while True:
    cmd = input('>>> ')

    if cmd == 'start':
        timer.start_t()

    elif cmd == 'stop':
        timer.stop_t()

    elif cmd == 'reset':
        timer.reset_t()

    elif cmd == 'exit':
        print(timer.total_time_day)
        break