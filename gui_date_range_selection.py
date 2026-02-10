import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

from utils import center_window


def create_date_range_window(parent: tk.Tk | tk.Toplevel, db_m: object, data: dict, subject: str, func) -> None:
    """
    Создает окно выбора периода истории предмета.
    :param parent: Родительское окно (главное окно выбора предметов).
    :param db_m: Объект класса DataBaseManager.
    :param data: Словарь с данными из базы.
    :param subject: Предмет.
    :param func: Callback-функция, вызываемая после выбора периода дат.
                 Принимает объект менеджера БД, отфильтрованные данные и имя предмета.
                 Используется для обновления отображаемых данных истории.
    """

    def show_date_range():
        """
        Получает выбранные даты из календарей.
        Фильтрует данные за указанный период.
        Передаёт отфильтрованные данные во внешнюю callback-функцию.
        """


        # забираем даты, форматируем
        date_from = datetime.strftime(cal_date_from.get_date(), '%Y-%m-%d')
        date_to = datetime.strftime(cal_date_to.get_date(), '%Y-%m-%d')

        # получаем новые данные
        data_filter = db_m.get_data_filter(data, subject, date_from, date_to)

        # передаём отфильтрованные данные через callback
        func(db_m, data_filter, subject)

        shell_dr.destroy()

    def update_start_date(event=None):
        """Изменяет дату в окончания периода календаре."""
        new_min = cal_date_from.get_date()
        cal_date_to.configure(mindate=new_min)

    def update_finish_date(event=None):
        """Изменяет дату в начала периода календаре."""
        new_max = cal_date_to.get_date()
        cal_date_from.configure(maxdate=new_max)

    # получение начальной даты истории предмета
    start_date = db_m.get_start_date_datetime(data, subject)
    # получение конечной даты истории предмета
    finish_date = db_m.get_finish_date_datetime(data, subject)

    # ---- GUI ----
    shell_dr = tk.Toplevel(parent)
    center_window(shell_dr, 300, 200)
    shell_dr.title("Выбор периода")
    shell_dr.resizable(False, False)
    label_d_from = tk.Label(shell_dr, text="Выберите начало периода", font=('Helvetica', 12))
    label_d_from.place(relx=0.5, rely=0.05, anchor='n')
    label_d_to = tk.Label(shell_dr, text="Выберите окончание периода", font=('Helvetica', 12))
    label_d_to.place(relx=0.5, rely=0.5, anchor='center')

    # окна выбора дат
    # начало периода
    cal_date_from = DateEntry(
        shell_dr,
        date_pattern="dd/mm/yyyy",
        font=('Helvetica', 10),
        year=start_date.year,
        month=start_date.month,
        day=start_date.day,
        width=20,
        locale="ru_RU",
        state="readonly",
        mindate=start_date,
        maxdate=finish_date
    )
    cal_date_from.place(relx=0.5, rely=0.20, anchor='n')

    # окончание периода
    cal_date_to = DateEntry(
        shell_dr,
        date_pattern="dd/mm/yyyy",
        font=('Helvetica', 10),
        year=finish_date.year,
        month=finish_date.month,
        day=finish_date.day,
        width=20,
        locale="ru_RU",
        state="readonly",
        mindate=start_date,
        maxdate=finish_date
    )
    cal_date_to.place(relx=0.5, rely=0.65, anchor='center')

    # обработчики событий
    cal_date_from.bind("<<DateEntrySelected>>", update_start_date)
    cal_date_to.bind("<<DateEntrySelected>>", update_finish_date)

    # кнопки управления
    btn_show = ttk.Button(shell_dr, text="Показать историю", command=show_date_range)

    # отображение кнопок
    btn_show.place(relx=0.5, rely=0.95, anchor='s')
