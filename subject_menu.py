"""Окно меню предмета (секундомер и история)."""
import customtkinter as ctk
from PIL import Image
import os


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
            text_color="#1D1D1F"
        )
        self.label_name.place(relx=0.06, rely=0.16, anchor="w")

        ctk.CTkLabel(
            self,
            text="Статистика и управление",
            font=("Segoe UI Semibold", 13),
            text_color="#86868B"
        ).place(relx=0.06, rely=0.24, anchor="w")

        # инфо-блок
        self.info = ctk.CTkFrame(
            self,
            fg_color="#F5F5F7",
            corner_radius=25,
            width=350,
            height=100
        )
        self.info.place(relx=0.5, rely=0.43, anchor="center")

        ctk.CTkLabel(
            self.info,
            text="СЕГОДНЯ",
            font=("Segoe UI Bold", 11),
            text_color="#86868B"
        ).place(relx=0.06, rely=0.25, anchor="nw")

        self.label_time = ctk.CTkLabel(
            self.info,
            text="",
            font=("Segoe UI Semibold", 30),
            text_color="#1D1D1F"
        )
        self.label_time.place(relx=0.06, rely=0.45, anchor="nw")

        # Кнопки управления
        base_path = os.path.dirname(__file__)

        arrow_img = ctk.CTkImage(
            light_image=Image.open(os.path.join(base_path, "assets", "icon_back.png")),
            size=(20, 20)
        )

        self.btn_back = ctk.CTkButton(
            self,
            text="",
            image=arrow_img,
            fg_color="transparent",
            hover_color="#F5F5F7",
            corner_radius=20,
            width=40,
            height=40,
            border_spacing=0,
            command=self.back
        )
        self.btn_back.place(relx=0.02, rely=0.07, anchor="w")

        self.btn_stopwatch = ctk.CTkButton(
            self,
            text="Секундомер",
            font=("Segoe UI Semibold", 15),
            text_color="#1D1D1F",
            fg_color="#D3E3FD",
            hover_color="#C1D5F0",
            corner_radius=29,
            width=350,
            height=58,
            command=self.open_stopwatch
        )
        self.btn_stopwatch.place(relx=0.5, rely=0.70, anchor="center")

        self.btn_history = ctk.CTkButton(
            self,
            text="Посмотреть историю",
            font=("Segoe UI Semibold", 15),
            text_color="#1D1D1F",
            fg_color="#F5F5F7",
            hover_color="#E5E5E7",
            corner_radius=29,
            width=350,
            height=58,
            command=self.open_history
        )
        self.btn_history.place(relx=0.5, rely=0.84, anchor="center")

    def on_show(self) -> None:
        """
        Обновляет информацию при показе страницы.
        """
        name = self.controller.current_subject
        if name:
            self.label_name.configure(text=name.upper())
            today_time = self.controller.get_time(name)
            self.label_time.configure(text=today_time)

    def open_stopwatch(self) -> None:
        """
        Открывает окно секундомера.
        """
        self.controller.open_stopwatch()

    def open_history(self) -> None:
        """
        Открывает окно с историей предмета.
        """
        self.controller.show_frame("History")

    def back(self) -> None:
        """
        Возвращает к окну выбора предметов.
        """
        self.controller.show_frame("StartWork")
