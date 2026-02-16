import tkinter as tk
from tkinter import ttk

from utils import center_window
from gui_date_range_selection import create_date_range_window


# ---- Логика ----


class History:

    def __init__(self):
        self.total_time = None
        self.total_days = None
        self.avg_time_sessions = None

    def refresh_data(self, db_m, new_data, subject):
        self.total_time.config(
            text=f"{db_m.get_total_time(new_data, subject)}"
        )
        self.total_days.config(
            text=f"{db_m.get_total_days(new_data, subject)}"
        )
        self.avg_time_sessions.config(
            text=f"{db_m.get_avg_time_session(new_data, subject)}"
        )

    def open_history_window(self, parent: tk.Tk | tk.Toplevel, db_m: object, data: dict, subject: str) -> None:
        """
        Создает окно History.
        :param parent: Родительское окно (главное окно выбора предметов).
        :param db_m: Объект класса DataBaseManager.
        :param data: Словарь с данными из базы.
        :param subject: Предмет.
        """

        def open_date_range_window():
            create_date_range_window(parent, db_m, data, subject, self.refresh_data)

        # ---- GUI ----
        shell_hist = tk.Toplevel(parent)
        shell_hist.title(f'History {subject}')
        center_window(shell_hist, 300, 200)
        shell_hist.resizable(False, False)

        # отображение информации
        tk.Label(
            shell_hist,
            text=f"Общее время '{subject}'/\nTotal time '{subject}'"
        ).pack()
        self.total_time = tk.Label(
            shell_hist,
            text=f"{db_m.get_total_time(data, subject)}",
            font=("Helvetica", 12, "bold"))
        self.total_time.pack()

        tk.Label(
            shell_hist,
            text=f"Общее кол-во дней '{subject}'/\nTotal number of days '{subject}'"
        ).pack()
        self.total_days = tk.Label(
            shell_hist,
            text=f"{db_m.get_total_days(data, subject)}",
            font=("Helvetica", 12, "bold"))
        self.total_days.pack()

        tk.Label(
            shell_hist,
            text=f"Среднее время сессии '{subject}'/\nAverage time session '{subject}'"
        ).pack()
        self.avg_time_sessions = tk.Label(
            shell_hist,
            text=f"{db_m.get_avg_time_session(data, subject)}",
            font=("Helvetica", 12, "bold"))
        self.avg_time_sessions.pack()

        # условие активации кнопки
        has_history = bool(data["subjects"][subject]["history"])
        button_state = 'normal' if has_history else 'disabled'

        # кнопки управления
        btn_date_range = ttk.Button(
            shell_hist,
            text="Выбрать период",
            state=button_state,
            command=open_date_range_window
        )

        # отображение кнопок
        btn_date_range.pack()
