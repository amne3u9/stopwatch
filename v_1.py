import time
from tkinter import *


class Stopwatch:

    def __init__(self):
        # общее время сессии за день
        self.total_time_day = []
        # флаг вкл./ выкл. секундомер
        self.running = False
        # начало отсчета
        self.start_time = 0.0
        # срез времени
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
            self.running = False
        elif self.total_t > 0.0:
            # сохранить total_t в 'время' сессии за день
            self.total_time_day.append(self.total_t)
        # в любом случае скидываем таймер
        self.total_t = 0.0

    def get_t(self):
        if self.running:
            return time.gmtime(self.total_t + (time.time() - self.start_time))
        return time.gmtime(self.total_t)


# ----GUI----
sw = Stopwatch()


def update_sw():
    now_time = time.strftime('%H:%M:%S', sw.get_t())
    label.config(text=now_time)
    shell_SW.after(200, update_sw)


def start():
    btn_start.pack_forget()
    btn_pause.pack()
    btn_reset.place(x=73, y=127)
    sw.start_t()
    update_sw()


def stop():
    btn_pause.pack_forget()
    btn_start.pack()
    btn_reset.place(x=73, y=127)
    sw.stop_t()


def reset():
    btn_reset.place_forget()
    btn_pause.pack_forget()
    btn_start.pack()
    sw.reset_t()


shell_SW = Tk()
shell_SW.title("StopWatch")
shell_SW.geometry('300x220')
shell_SW.resizable(width=False, height=False)
label = Label(shell_SW, font=('Times New Roman', 30), text='00:00:00')
label.pack()

btn_start = Button(shell_SW, width=8, font=('Times New Roman', 25), text='START', bg='light green', command=start)
btn_pause = Button(shell_SW, width=8, font=('Times New Roman', 25), text='STOP', bg='brown', fg='white', command=stop)
btn_reset = Button(shell_SW, width=8, font=('Times New Roman', 25), text='RESET', bg='black', fg='white', command=reset)
btn_start.pack()

shell_SW.mainloop()
