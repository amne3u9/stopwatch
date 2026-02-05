import tkinter as tk
from utils import center_window


# ---- Логика ----


class History:

    def open_history_window(self, parent: tk, db_m: object, data: dict, subject: str) -> None:
        """
        Создает окно History.
        :param parent: Родительское окно (главное окно выбора предметов).
        :param db_m: Объект класса DataBaseManager.
        :param data: Словарь с данными из базы.
        :param subject: Предмет.
        """

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
        label_total_t = tk.Label(
            shell_hist,
            text=f"{db_m.get_total_time(data, subject)}",
            font=("Helvetica", 12, "bold"))
        label_total_t.pack()

        tk.Label(
            shell_hist,
            text=f"Общее кол-во дней '{subject}'/\nTotal number of days '{subject}'"
        ).pack()
        label_total_d = tk.Label(
            shell_hist,
            text=f"{db_m.get_total_days(data, subject)}",
            font=("Helvetica", 12, "bold"))
        label_total_d.pack()

        tk.Label(
            shell_hist,
            text=f"Среднее время сессии '{subject}'/\nAverage time session '{subject}'"
        ).pack()
        label_avg_t = tk.Label(
            shell_hist,
            text=f"{db_m.get_avg_time_session(data, subject)}",
            font=("Helvetica", 12, "bold"))
        label_avg_t.pack()
