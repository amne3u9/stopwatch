"""Окно меню предмета (Stopwatch / History / Back)."""
import tkinter as tk
from tkinter import ttk
from utils import center_window
from gui_stopwatch import open_stopwatch_window


def creation_menu_subject(parent: tk, name: str) -> None:
    """
    Создает окно с кнопками "Stopwatch", "History", "Back".
    :param parent: Родительское окно (главное окно выбора предметов).
    :param name: Предмет.
    """

    def open_stopwatch() -> None:
        """
        Открывает окно секундомера.
        """
        open_stopwatch_window(parent, name)

    def open_history() -> None:
        """
        Открывает окно с историей.
        """
        pass

    def back_to() -> None:
        """
        Уничтожает окно с кнопками.
        Разворачивает окно с выбором предметов.
        """
        menu_subject.destroy()
        parent.deiconify()

    menu_subject = tk.Toplevel(parent)
    menu_subject.title(f'Menu {name}')
    center_window(menu_subject, 250, 160)
    menu_subject.resizable(False, False)
    menu_subject.protocol("WM_DELETE_WINDOW", back_to)

    # Изменение стиля кнопок
    s = ttk.Style()
    s.configure("Big.TButton", padding=13)

    # Кнопки управления
    btn_stopwatch = ttk.Button(
        menu_subject,
        text="S T O P W A T C H",
        width=30,
        style="Big.TButton",
        command=open_stopwatch
    )
    btn_history = ttk.Button(
        menu_subject,
        text="H I S T O R Y",
        width=30,
        style="Big.TButton",
        command=open_history
    )
    btn_back = ttk.Button(
        menu_subject,
        text="B A C K",
        width=34,
        command=back_to
    )

    # Отображение кнопок
    btn_stopwatch.place(relx=0.5, rely=0.05, anchor='n')
    btn_history.place(relx=0.5, rely=0.55, anchor='center')
    btn_back.place(relx=0.5, rely=0.95, anchor='s')
