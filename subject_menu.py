"""Окно меню предмета (Stopwatch / History )."""
import customtkinter as ctk

from gui_stopwatch import open_stopwatch_window


class SubjectActions(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.window_title = "Меню предмета"
        self.configure(fg_color="transparent")

        self.label_name = ctk.CTkLabel(
            self,
            text="",
            font=("Segoe UI Semibold", 20),
            text_color='#1D1D1F'
        )
        self.label_name.place(relx=0.06, rely=0.16, anchor='w')

        ctk.CTkLabel(
            self,
            text="Статистика и управление",
            font=("Segoe UI Semibold", 13),
            text_color='#86868B'
        ).place(relx=0.06, rely=0.24, anchor='w')

        # инфо-блок
        self.info = ctk.CTkFrame(
            self,
            fg_color='#F5F5F7',
            corner_radius=25,
            width=350,
            height=100
        )
        self.info.place(relx=0.5, rely=0.43, anchor='center')

        ctk.CTkLabel(
            self.info,
            text="СЕГОДНЯ",
            font=("Segoe UI Bold", 11),
            text_color='#86868B'
        ).place(relx=0.06, rely=0.25, anchor='nw')

        self.label_time = ctk.CTkLabel(
            self.info,
            text="",
            font=("Segoe UI Semibold", 30),
            text_color='#1D1D1F'
        )
        self.label_time.place(relx=0.06, rely=0.45, anchor='nw')

        # Кнопки управления
        self.btn_stopwatch = ctk.CTkButton(
            self,
            text="СЕКУНДОМЕР",
            font=("Segoe UI Semibold", 14),
            text_color='#1D1D1F',
            fg_color='#D3E3FD',
            hover_color="#C1D5F0",
            corner_radius=29,
            width=350,
            height=58,
            command=self.open_stopwatch
        )
        self.btn_stopwatch.place(relx=0.5, rely=0.70, anchor='center')

        self.btn_history = ctk.CTkButton(
            self,
            text="ПОСМОТРЕТЬ ИСТОРИЮ",
            font=("Segoe UI Semibold", 14),
            text_color='#1D1D1F',
            fg_color='#F5F5F7',
            hover_color="#E5E5E7",
            corner_radius=29,
            width=350,
            height=58,
            command=self.open_history
        )
        self.btn_history.place(relx=0.5, rely=0.84, anchor='center')

        self.btn_back = ctk.CTkButton(
            self,
            text="←",
            font=("Segoe UI Semibold", 24),
            text_color='#1D1D1F',
            fg_color="transparent",
            hover_color='#F5F5F7',
            corner_radius=20,
            width=40,
            height=40,
            border_spacing=0,
            command=self.back
        )
        self.btn_back.place(relx=0.02, rely=0.07, anchor='w')
        self.btn_back._text_label.grid_configure(pady=(0, 8))

    def on_show(self):
        name = self.controller.current_subject
        if name:
            self.label_name.configure(text=name.upper())
            time = self.controller.get_time(name)
            self.label_time.configure(text=time)

    def open_stopwatch(self) -> None:
        """
        Открывает окно секундомера.
        """
        open_stopwatch_window(self.controller, self.controller.current_subject)

    def open_history(self) -> None:
        """
        Открывает окно с историей предмета.
        """
        self.controller.show_frame("History")

    def back(self) -> None:
        """
        Разворачивает окно с выбором предметов.
        """
        self.controller.show_frame("StartWork")
