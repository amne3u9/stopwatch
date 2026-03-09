import customtkinter as ctk
import sys


def center_window(main: ctk.CTk, width: int, height: int) -> None:
    """
    Центрирует главное окно на экране.
    :param main: Объект CTk().
    :param width: Ширина окна.
    :param height: Высота окна.
    """
    # размеры экрана(ширина, высота)
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    # вычисление координат(x, y)
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # проверка на OC
    if sys.platform != "darwin":
        # коэффициент масштабирования
        scaling = main._get_window_scaling()
        x = int(x * scaling)
        y = int(y * scaling)

    main.geometry(f"{width}x{height}+{x}+{y}")


def extra_window(main: ctk.CTk, window: ctk.CTkToplevel, width: int, height: int) -> None:
    """
    Задаёт положение дополнительных окон в центре родительского.
    :param main: Главное окно.
    :param window: Новое окно.
    :param width: Ширина окна.
    :param height: Высота окна.
    """
    # обновляем интерфейс
    main.update_idletasks()
    window.update_idletasks()

    # координаты родительского окна
    x_main = main.winfo_x()
    y_main = main.winfo_y()
    # размеры родительского окна(ширина, высота)
    main_width = main.winfo_width()
    main_height = main.winfo_height()

    # вычисление координат(x, y)
    if sys.platform != "darwin":
        # коэффициент масштабирования
        scaling = main._get_window_scaling()
        x = x_main + (main_width - width * scaling) // 2
        y = y_main + (main_height - height * scaling) // 2
    else:
        x = x_main + (main_width - width) // 2
        y = y_main + (main_height - height) // 2

    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


def stopwatch_position(main: ctk.CTk, window: ctk.CTkToplevel, width: int, height: int) -> None:
    """
    Располагает окно секундомера справа или слева от главного окна.
    :param main: Главное окно.
    :param window: Toplevel.
    :param width: Ширина окна Toplevel.
    :param height: Высота окна Toplevel.
    """
    # обновляем интерфейс
    main.update_idletasks()
    window.update_idletasks()

    # коэффициент масштабирования
    scaling = main._get_window_scaling()
    # размеры экрана(по ширине)
    screen_width = main.winfo_screenwidth()
    # координаты родительского окна
    x_main = main.winfo_x()
    y_main = main.winfo_y()
    # размеры родительского окна(по ширине)
    main_width = main.winfo_width()

    # вычисление координат(x, y)
    y = y_main + 20
    # определяем сторону с учётом масштабирования
    if screen_width >= (x_main + main_width) // scaling + width + 10:
        x = x_main + main_width + 10
    else:
        x = x_main - int(width * scaling + 10)

    window.geometry(f"{width}x{height}+{x}+{y}")


def offset_window(main: ctk.CTk, window: ctk.CTkToplevel, width: int, height: int) -> None:
    """
    Смещает окно относительно главного окна.
    :param main: Главное окно.
    :param window: Toplevel.
    :param width: Ширина окна.
    :param height: Высота окна.
    """
    # обновляем интерфейс
    main.update_idletasks()
    window.update_idletasks()

    # коэффициент масштабирования
    scaling = main._get_window_scaling()
    # размеры экрана(по ширине)
    screen_width = main.winfo_screenwidth()
    # координаты родительского окна
    x_main = main.winfo_x()
    y_main = main.winfo_y()

    # вычисление координат(x, y)
    y = y_main + 50
    if screen_width >= x_main // scaling + width + 30:
        x = x_main + 30
    else:
        x = x_main - 30

    window.geometry(f"{width}x{height}+{x}+{y}")
