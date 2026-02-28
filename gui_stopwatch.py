import time
import customtkinter as ctk

from stopwatch import Stopwatch
from utils import stopwatch_window, center_window


def open_stopwatch_window(parent: ctk.CTk, subject: str) -> None:
    sw = Stopwatch()
    # ---- GUI ----
    new_window = ctk.CTkToplevel(parent)
    new_window.title("Секундомер")
    stopwatch_window(parent, new_window, 320, 240)
    new_window.resizable(width=False, height=False)
    new_window.configure(fg_color='#FFFFFF')
    new_window.transient(parent)

    ctk.CTkLabel(
        new_window,
        text="ТАЙМЕР АКТИВНОСТИ",
        font=("Segoe UI Semibold", 11),
        text_color='#86868B'
    ).place(relx=0.5, rely=0.10, anchor="center")

    # циферблат
    clock_face = ctk.CTkFrame(
        new_window,
        fg_color='#F5F5F7',
        corner_radius=20,
        width=280,
        height=80
    )
    clock_face.place(relx=0.5, rely=0.40, anchor="center")

    # отображение времени
    label_time = ctk.CTkLabel(
        clock_face,
        text='00:00:00',
        font=("Segoe UI Semibold", 45),
        text_color="#1D1D1F"
    )
    label_time.place(relx=0.5, rely=0.5, anchor='center')

    def update_ui() -> None:
        """
        Обновляет label_time с текущим временем секундомера каждые 200 мс.
        Вызывает саму себя рекурсивно через after().
        """
        if sw.running:
            now_time = time.strftime('%H:%M:%S', sw.get_t())
            label_time.configure(text=now_time)
            new_window.after(200, update_ui)
        else:
            now_time = time.strftime('%H:%M:%S', sw.get_t())
            label_time.configure(text=now_time)

    def start() -> None:
        """
        Запускает секундомер.
        Скрывает кнопку СТАРТ, показывает кнопку СТОП и СБРОС.
        Запускает обновление времени через update_sw().
        """
        btn_start.place_forget()
        btn_pause.place(relx=0.30, rely=0.77, anchor="center")
        btn_reset.place(relx=0.70, rely=0.77, anchor="center")
        sw.start_t()
        update_ui()

    def stop() -> None:
        """
        Останавливает секундомер.
        Скрывает кнопку СТОП, показывает СТАРТ.
        СБРОС остаётся доступен.
        """
        btn_pause.place_forget()
        btn_start.configure(
            corner_radius=20,
            width=120,
            height=40)
        btn_start.place(relx=0.30, rely=0.77, anchor="center")
        btn_reset.place(relx=0.70, rely=0.77, anchor="center")
        sw.stop_t()

    def reset() -> None:
        """
        Сбрасывает секундомер и добавляет прошедшее время.
        Скрывает СБРОС и СТОП, показывает СТАРТ.
        """
        btn_reset.place_forget()
        btn_pause.place_forget()
        btn_start.configure(
            corner_radius=21,
            width=250,
            height=42)
        btn_start.place(relx=0.5, rely=0.77, anchor="center")
        parent.add_session(subject, sw.reset_t())
        update_ui()

    def create_force_quit_window() -> None:
        """Создает информационное окно экстренного закрытия секундомера."""

        force_quit_window = ctk.CTkToplevel(parent)
        force_quit_window.title("Экстренное завершение")
        center_window(force_quit_window, 320, 240)
        force_quit_window.resizable(width=False, height=False)
        force_quit_window.configure(fg_color='#FFFFFF')
        force_quit_window.grab_set()

        ctk.CTkLabel(
            force_quit_window,
            text=f"Секундомер активен,\n хотите сохранить результат?",
            font=("Segoe UI Semibold", 14),
            text_color='#1D1D1F'
        ).place(relx=0.5, rely=0.30, anchor='center')

        def btn_yes() -> None:
            parent.add_session(subject, sw.reset_t())
            force_quit_window.destroy()
            new_window.destroy()

        def btn_no() -> None:
            force_quit_window.destroy()
            new_window.destroy()

        # кнопки управления окна предупреждения ДА/НЕТ
        ctk.CTkButton(
            force_quit_window,
            text="ДА",
            font=("Segoe UI Semibold", 13),
            text_color='#1D1D1F',
            fg_color='#D3E3FD',
            hover_color="#C1D5F0",
            corner_radius=20,
            width=100,
            height=40,
            command=btn_yes
        ).place(relx=0.30, rely=0.77, anchor="center")

        ctk.CTkButton(
            force_quit_window,
            text="НЕТ",
            font=("Segoe UI Semibold", 13),
            text_color='#1D1D1F',
            fg_color='#F5F5F7',
            hover_color="#E5E5E7",
            corner_radius=20,
            width=100,
            height=40,
            command=btn_no
        ).place(relx=0.70, rely=0.77, anchor="center")

    def force_quit() -> None:
        """
        Узнает о состоянии секундомера.
        При необходимости открывает информационное окно.
        """
        if sw.running:
            stop()
            create_force_quit_window()
        else:
            if sw.total_t > 0:
                create_force_quit_window()
            else:
                new_window.destroy()

    # Кнопки управления
    btn_start = ctk.CTkButton(
        new_window,
        text='СТАРТ',
        font=("Segoe UI Semibold", 13),
        text_color="#FFFFFF",
        fg_color="#34A853",
        hover_color="#2E8B46",
        corner_radius=21,
        width=250,
        height=42,
        command=start
    )
    btn_start.place(relx=0.5, rely=0.77, anchor="center")

    btn_pause = ctk.CTkButton(
        new_window,
        text='СТОП',
        font=("Segoe UI Semibold", 13),
        text_color="#FFFFFF",
        fg_color="#EA4335",
        hover_color="#D93025",
        corner_radius=20,
        width=120,
        height=40,
        command=stop
    )

    btn_reset = ctk.CTkButton(
        new_window,
        text='СБРОС',
        font=("Segoe UI Semibold", 13),
        text_color='#1D1D1F',
        fg_color='#F5F5F7',
        hover_color="#E5E5E7",
        corner_radius=20,
        width=120,
        height=40,
        command=reset
    )
    new_window.protocol("WM_DELETE_WINDOW", force_quit)
