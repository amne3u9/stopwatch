import time
import customtkinter as ctk

from stopwatch import Stopwatch
from utils import stopwatch_position, extra_window


class StopwatchWindow(ctk.CTkToplevel):
    def __init__(self, parent, subject):
        super().__init__(parent)
        self.parent = parent
        self.subject = subject
        self.stopwatch = Stopwatch()

        stopwatch_position(self.parent, self, 320, 240)
        self.title("Секундомер")
        self.resizable(width=False, height=False)
        self.configure(fg_color="#FFFFFF")
        self.protocol("WM_DELETE_WINDOW", self.closing_check)

        ctk.CTkLabel(
            self,
            text="ТАЙМЕР АКТИВНОСТИ",
            font=("Segoe UI Semibold", 11),
            text_color="#86868B"
        ).place(relx=0.5, rely=0.10, anchor="center")

        # циферблат
        self.clock_face = ctk.CTkFrame(
            self,
            fg_color="#F5F5F7",
            corner_radius=20,
            width=280,
            height=80
        )
        self.clock_face.place(relx=0.5, rely=0.40, anchor="center")

        # отображение времени
        self.label_time = ctk.CTkLabel(
            self.clock_face,
            text="00:00:00",
            font=("Segoe UI Semibold", 45),
            text_color="#1D1D1F"
        )
        self.label_time.place(relx=0.5, rely=0.5, anchor="center")

        # Кнопки управления
        self.btn_start = ctk.CTkButton(
            self,
            text="Старт",
            font=("Segoe UI Semibold", 13),
            text_color="#FFFFFF",
            fg_color="#34A853",
            hover_color="#2E8B46",
            corner_radius=21,
            width=250,
            height=42,
            command=self.start
        )
        self.btn_start.place(relx=0.5, rely=0.77, anchor="center")

        self.btn_pause = ctk.CTkButton(
            self,
            text="Стоп",
            font=("Segoe UI Semibold", 13),
            text_color="#FFFFFF",
            fg_color="#EA4335",
            hover_color="#D93025",
            corner_radius=21,
            width=120,
            height=42,
            command=self.stop
        )

        self.btn_reset = ctk.CTkButton(
            self,
            text="Сброс",
            font=("Segoe UI Semibold", 13),
            text_color="#1D1D1F",
            fg_color="#F5F5F7",
            hover_color="#E5E5E7",
            corner_radius=21,
            width=120,
            height=42,
            command=self.reset
        )

    def update_ui(self) -> None:
        """
        Обновляет label_time с текущим временем секундомера каждые 200 мс.
        Вызывает саму себя рекурсивно через after().
        """
        now_time = time.strftime("%H:%M:%S", self.stopwatch.get_t())
        self.label_time.configure(text=now_time)

        if self.stopwatch.running:
            self.after(200, self.update_ui)

    def start(self) -> None:
        """
        Запускает секундомер.
        Скрывает кнопку Старт, показывает кнопку Стоп и Сброс.
        Запускает обновление времени через update_sw().
        """
        self.btn_start.place_forget()
        self.btn_pause.place(relx=0.30, rely=0.77, anchor="center")
        self.btn_reset.place(relx=0.70, rely=0.77, anchor="center")
        self.stopwatch.start_t()
        self.update_ui()

    def stop(self) -> None:
        """
        Останавливает секундомер.
        Скрывает кнопку Стоп, показывает Старт.
        Сброс остаётся доступен.
        """
        self.btn_pause.place_forget()
        self.btn_start.configure(
            corner_radius=21,
            width=120,
            height=42)
        self.btn_start.place(relx=0.30, rely=0.77, anchor="center")
        self.btn_reset.place(relx=0.70, rely=0.77, anchor="center")
        self.stopwatch.stop_t()

    def reset(self) -> None:
        """
        Сбрасывает секундомер и сохраняет прошедшее время.
        Скрывает Сброс и Стоп, показывает Старт.
        """
        self.btn_reset.place_forget()
        self.btn_pause.place_forget()
        self.btn_start.configure(
            corner_radius=21,
            width=250,
            height=42)
        self.btn_start.place(relx=0.5, rely=0.77, anchor="center")
        self.parent.add_session(self.subject, *self.stopwatch.reset_t())
        self.update_ui()

    def create_force_quit_window(self, close_app: bool) -> None:
        """
        Создает информационное окно экстренного закрытия секундомера.
        Если close_app = True, закроется все приложение.
        :param close_app: Указывает, нужно ли закрыть всё приложение.
        """

        force_quit_window = ctk.CTkToplevel(self.parent)
        force_quit_window.title("Экстренное завершение")
        extra_window(self.parent, force_quit_window, 320, 240)
        force_quit_window.resizable(width=False, height=False)
        force_quit_window.configure(fg_color="#FFFFFF")
        force_quit_window.grab_set()

        ctk.CTkLabel(
            force_quit_window,
            text=f"Секундомер активен,\n хотите сохранить результат?",
            font=("Segoe UI Semibold", 13),
            text_color="#1D1D1F"
        ).place(relx=0.5, rely=0.30, anchor="center")

        def selection_result(save: bool = True) -> None:
            """
            Обрабатывает результат выбора пользователя.
            :param save: Флаг о добавлении сессии.
            """
            if save:
                self.parent.add_session(self.subject, *self.stopwatch.reset_t())
            force_quit_window.destroy()
            self.destroy()
            self.parent.stopwatch_closed()
            if close_app:
                self.parent.destroy()

        # кнопки управления окна предупреждения ДА/НЕТ
        ctk.CTkButton(
            force_quit_window,
            text="Да",
            font=("Segoe UI Semibold", 13),
            text_color="#1D1D1F",
            fg_color="#D3E3FD",
            hover_color="#C1D5F0",
            corner_radius=20,
            width=100,
            height=40,
            command=lambda: selection_result(True)
        ).place(relx=0.30, rely=0.77, anchor="center")

        ctk.CTkButton(
            force_quit_window,
            text="Нет",
            font=("Segoe UI Semibold", 13),
            text_color="#1D1D1F",
            fg_color="#F5F5F7",
            hover_color="#E5E5E7",
            corner_radius=20,
            width=100,
            height=40,
            command=lambda: selection_result(False)
        ).place(relx=0.70, rely=0.77, anchor="center")

    def closing_check(self, close_app: bool = False) -> None:
        """
        Проверяет состояние секундомера.
        При необходимости открывает информационное окно.
        :param close_app: Указывает, нужно ли закрыть всё приложение.
        """
        if self.stopwatch.running:
            self.stop()
            self.create_force_quit_window(close_app)
        else:
            if self.stopwatch.total_t > 0:
                self.create_force_quit_window(close_app)
            else:
                self.destroy()
                self.parent.stopwatch_closed()
                if close_app:
                    self.parent.destroy()

    def stop_work(self) -> bool:
        if self.stopwatch.running:
            self.stop()
        return True
