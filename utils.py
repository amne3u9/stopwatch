import customtkinter as ctk


def center_window(main: ctk.CTk, width: int, height: int) -> None:
    """
    Центрирует окно на экране.
    :param main: Объект CTk().
    :param width: Ширина окна.
    :param height: Высота окна.
    """
    # коэффициент масштабирования
    scaling = main._get_window_scaling()
    # размеры экрана(ширина, высота)
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    # вычисление координат(x, y)
    x = int(((screen_width - width) // 2) * scaling)
    y = int(((screen_height - height) // 2) * scaling)

    main.geometry(f"{width}x{height}+{x}+{y}")


def extra_window(main: ctk.CTk, window: ctk.CTkToplevel, width: int, height: int) -> None:
    """
    Задаёт положение дополнительных окон в центре родительского.
    :param main: Главное окно.
    :param window: Новое окно.
    :param width: Ширина окна.
    :param height: Высота окна.
    """

    # коэффициент масштабирования
    scaling = main._get_window_scaling()
    # координаты родительского окна
    x_main = main.winfo_x()
    y_main = main.winfo_y()
    # размеры родительского окна(ширина, высота)
    main_width = main.winfo_width()
    main_height = main.winfo_height()
    # вычисление координат(x, y)
    x = int(x_main + (main_width - width * scaling) // 2)
    y = int(y_main + (main_height - height * scaling) // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")


def stopwatch_window(main: ctk.CTk, window: ctk.CTkToplevel, width: int, height: int) -> None:
    """
    Располагает окно секундомера справа или слева от главного окна.
    :param main: Главное окно.
    :param window: Toplevel.
    :param width: Ширина окна Toplevel.
    :param height: Высота окна Toplevel.
    """
    # коэффициент масштабирования
    scaling = main._get_window_scaling()
    # размеры экрана(по ширине)
    screen_width = main.winfo_screenwidth()
    # координаты родительского окна
    x_main = main.winfo_x()
    y_main = main.winfo_y()
    # размеры родительского окна(по ширине)
    main_width = main.winfo_width()

    # определяем сторону
    # условие с учётом масштабирования
    size_place = (x_main + main_width) // scaling + width + 10
    if screen_width >= size_place:
        x = x_main + main_width + 10
        y = y_main + 20
    else:
        x = x_main - int(width * scaling + 10)
        y = y_main + 20

    window.geometry(f"{width}x{height}+{x}+{y}")


def offset_window(main: ctk.CTk, window: ctk.CTkToplevel, width: int, height: int) -> None:
    """
    Смещает окно относительно главного окна.
    :param main: Главное окно.
    :param window: Toplevel.
    :param width: Ширина окна.
    :param height: Высота окна.
    """
    # коэффициент масштабирования
    scaling = main._get_window_scaling()

    # размеры экрана(по ширине)
    screen_width = main.winfo_screenwidth()
    # координаты родительского окна
    x_main = main.winfo_x()
    y_main = main.winfo_y()

    if screen_width >= x_main // scaling + 30 + width:
        x = x_main + 30
        y = y_main + 50
    else:
        x = x_main - 30
        y = y_main + 50

    window.geometry(f"{width}x{height}+{x}+{y}")
