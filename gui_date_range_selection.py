import customtkinter as ctk
from tkcalendar import DateEntry
from datetime import datetime

from utils import offset_window


def ask_date_range(parent: ctk.CTk | ctk.CTkToplevel, callback) -> None:
    """
    Создает окно выбора периода истории предмета.
    :param parent: Родительское окно (App).
    :param callback: Callback-функция, вызываемая после выбора периода дат.
                 Отфильтрованные данные и имя предмета.
                 Используется для обновления отображаемых данных истории.
    """

    # ---- GUI ----
    new_window = ctk.CTkToplevel(parent)
    new_window.title("Выбор периода")
    offset_window(parent, new_window, 400, 400)
    new_window.resizable(False, False)
    new_window.configure(fg_color='#FFFFFF')
    new_window.grab_set()

    ctk.CTkLabel(
        new_window,
        text="ВЫБОР ПЕРИОДА",
        font=("Segoe UI Semibold", 20),
        text_color='#1D1D1F'
    ).place(relx=0.06, rely=0.08, anchor='w')

    ctk.CTkLabel(
        new_window,
        text='Укажите временной диапазон',
        font=("Segoe UI Semibold", 13),
        text_color='#86868B'
    ).place(relx=0.06, rely=0.20, anchor='w')

    # блоки выбора дат

    # блок начала диапазона
    card_start = ctk.CTkFrame(
        new_window,
        fg_color='#F5F5F7',
        corner_radius=21,
        width=350,
        height=85
    )
    card_start.place(relx=0.5, rely=0.36, anchor="center")

    ctk.CTkLabel(
        card_start,
        text="НАЧАЛО ПЕРИОДА",
        font=("Segoe UI Bold", 11),
        text_color='#86868B'
    ).place(relx=0.07, rely=0.13, anchor="nw")

    # блок окончания диапазона
    card_end = ctk.CTkFrame(
        new_window,
        fg_color='#F5F5F7',
        corner_radius=21,
        width=350,
        height=85
    )
    card_end.place(relx=0.5, rely=0.61, anchor="center")

    ctk.CTkLabel(
        card_end,
        text="КОНЕЦ ПЕРИОДА",
        font=("Segoe UI Bold", 11),
        text_color='#86868B'
    ).place(relx=0.07, rely=0.13, anchor="nw")

    def show_date_range():
        """
        Забирает выбранные даты из календарей.
        Фильтрует данные за указанный период.
        Передаёт отфильтрованные данные во внешнюю callback-функцию.
        """

        # забираем даты, форматируем
        date_from = cal_start.get_date().strftime('%Y-%m-%d')
        date_to = cal_end.get_date().strftime('%Y-%m-%d')

        # получаем новые данные
        data_filter = parent.get_data_filter(date_from, date_to)

        # передаём отфильтрованные данные через callback
        callback(data_filter, parent.current_subject)

        new_window.destroy()

    def update_start_date(event=None):
        """Изменяет начала периода в календаре cal_end."""
        new_min = cal_start.get_date()
        cal_end.configure(mindate=new_min)

    def update_end_date(event=None):
        """Изменяет окончание периода в календаре cal_start."""
        new_max = cal_end.get_date()
        cal_start.configure(maxdate=new_max)

    # получение начальной даты истории предмета
    start_date = datetime.strptime(parent.get_start_date(), '%Y-%m-%d').date()
    # получение конечной даты истории предмета
    end_date = datetime.strptime(parent.get_end_date(), '%Y-%m-%d').date()

    # календари выбора дат

    # начало периода
    cal_start = DateEntry(
        card_start,
        date_pattern="dd/mm/yyyy",
        font=("Segoe UI Semibold", 15),
        year=start_date.year,
        month=start_date.month,
        day=start_date.day,
        locale="ru_RU",
        state="readonly",
        mindate=start_date,
        maxdate=end_date,
        background='#D3E3FD',
        foreground='#1D1D1F',
        borderwidth=0,
        highlightthickness=0,
        selectbackground='#007AFF',
        selectforeground='#FFFFFF',
        headersbackground='#F5F5F7',
        headersforeground='#86868B',
        normalbackground='#FFFFFF',
        normalforeground='#1D1D1F',
        weekendbackground='#FFFFFF',
        weekendforeground='#007AFF',
        othermonthbackground='#FFFFFF',
        othermonthforeground='#E5E5EA',
        othermonthwebackground='#FFFFFF',
        othermonthweforeground='#E5E5EA'
    )
    cal_start.place(relx=0.07, rely=0.48, anchor="nw", relwidth=0.84)

    # окончание периода
    cal_end = DateEntry(
        card_end,
        date_pattern="dd/mm/yyyy",
        font=("Segoe UI Semibold", 15),
        year=end_date.year,
        month=end_date.month,
        day=end_date.day,
        locale="ru_RU",
        state="readonly",
        mindate=start_date,
        maxdate=end_date,
        background='#D3E3FD',
        foreground='#1D1D1F',
        borderwidth=0,
        highlightthickness=0,
        selectbackground='#007AFF',
        selectforeground='#FFFFFF',
        headersbackground='#F5F5F7',
        headersforeground='#86868B',
        normalbackground='#FFFFFF',
        normalforeground='#1D1D1F',
        weekendbackground='#FFFFFF',
        weekendforeground='#007AFF',
        othermonthbackground='#FFFFFF',
        othermonthforeground='#E5E5EA',
        othermonthwebackground='#FFFFFF',
        othermonthweforeground='#E5E5EA'
    )
    cal_end.place(relx=0.07, rely=0.48, anchor="nw", relwidth=0.84)

    # обработчики событий
    cal_start.bind("<<DateEntrySelected>>", update_start_date)
    cal_end.bind("<<DateEntrySelected>>", update_end_date)

    # кнопки управления
    btn_show = ctk.CTkButton(
        new_window,
        text="ПРИМЕНИТЬ",
        font=("Segoe UI Semibold", 14),
        text_color='#1D1D1F',
        fg_color='#D3E3FD',
        hover_color="#C1D5F0",
        corner_radius=25,
        width=350,
        height=50,
        command=show_date_range
    )
    btn_show.place(relx=0.5, rely=0.88, anchor='center')
