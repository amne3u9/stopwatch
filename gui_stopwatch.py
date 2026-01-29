import time
from tkinter import *
from session_manager import SessionManager
from stopwatch import Stopwatch

# ---- Логика ----
sw = Stopwatch()
sm = SessionManager()


def update_sw() -> None:
    """
    Обновляет Label с текущим временем секундомера каждые 200 мс.
    Вызывает саму себя рекурсивно через after().
    """
    now_time = time.strftime('%H:%M:%S', sw.get_t())
    label.config(text=now_time)
    shell_SW.after(200, update_sw)


def start() -> None:
    """
    Запускает секундомер.
    Скрывает кнопку START, показывает кнопку STOP и RESET.
    Запускает обновление времени через update_sw().
    """
    btn_start.pack_forget()
    btn_pause.pack()
    btn_reset.place(x=73, y=127)
    sw.start_t()
    update_sw()


def stop() -> None:
    """
    Останавливает секундомер.
    Скрывает кнопку STOP, показывает START.
    RESET остаётся доступен.
    """
    btn_pause.pack_forget()
    btn_start.pack()
    btn_reset.place(x=73, y=127)
    sw.stop_t()


def reset() -> None:
    """
    Сбрасывает секундомер и добавляет прошедшее время в SessionManager.
    Скрывает RESET и STOP, показывает START.
    """
    btn_reset.place_forget()
    btn_pause.pack_forget()
    btn_start.pack()
    sm.add_session(sw.reset_t())


# ---- GUI ----
shell_SW = Tk()
shell_SW.title("StopWatch")
shell_SW.geometry('300x220')
shell_SW.resizable(width=False, height=False)

# Label отображение времени
label = Label(shell_SW, font=('Times New Roman', 30), text='00:00:00')
label.pack()

# Кнопки управления
btn_start = Button(shell_SW, width=8, font=('Times New Roman', 25), text='START', bg='light green', command=start)
btn_pause = Button(shell_SW, width=8, font=('Times New Roman', 25), text='STOP', bg='brown', fg='white', command=stop)
btn_reset = Button(shell_SW, width=8, font=('Times New Roman', 25), text='RESET', bg='black', fg='white', command=reset)
btn_start.pack()

# Запуск окна
shell_SW.mainloop()
