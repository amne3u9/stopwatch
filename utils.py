from tkinter import *


def center_window(window: Tk | Toplevel, width: int, height: int) -> None:
    """
    Центрирует окно на экране.
    :param window: Объект Tk() или TopLevel().
    :param width: Ширина окна.
    :param height: Высота окна.
    """
    # ширина экрана
    screen_width = window.winfo_screenwidth()
    # высота экрана
    screen_height = window.winfo_screenheight()
    # вычисление координат по x
    x = (screen_width - width) // 2
    # вычисление координат по y
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")
