import time
import tkinter as tk
from stopwatch import Stopwatch
from db_manager import DataBaseManager

# ---- Логика ----
sw = Stopwatch()
db_m = DataBaseManager()


def open_stopwatch_window(parent: tk, subject: str) -> None:
    def update_sw() -> None:
        """
        Обновляет Label с текущим временем секундомера каждые 200 мс.
        Вызывает саму себя рекурсивно через after().
        """
        now_time = time.strftime('%H:%M:%S', sw.get_t())
        label.config(text=now_time)
        shell_sw.after(200, update_sw)

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
        db_m.add_session(subject, sw.reset_t())

    # ---- GUI ----
    shell_sw = tk.Toplevel(parent)
    shell_sw.title("StopWatch")
    shell_sw.geometry('300x220')
    shell_sw.resizable(width=False, height=False)

    # Label отображение времени
    label = tk.Label(shell_sw, font=('Times New Roman', 30), text='00:00:00')
    label.pack()

    # Кнопки управления
    btn_start = tk.Button(
        shell_sw,
        width=8,
        font=('Times New Roman', 25),
        text='START', bg='light green',
        command=start
    )
    btn_pause = tk.Button(
        shell_sw,
        width=8,
        font=('Times New Roman', 25),
        text='STOP',
        bg='brown',
        fg='white',
        command=stop
    )
    btn_reset = tk.Button(
        shell_sw,
        width=8,
        font=('Times New Roman', 25),
        text='RESET',
        bg='black',
        fg='white',
        command=reset
    )

    # Отображение кнопок
    btn_start.pack()
