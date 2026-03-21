import customtkinter as ctk
from PIL import Image

from gui_date_range_selection import ask_date_range


class History(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pm = self.controller.path_manager
        self.window_title = "История предмета"
        self.configure(fg_color="transparent")

        self.label_name = ctk.CTkLabel(
            self,
            text="",
            font=("Segoe UI Semibold", 20),
            text_color="#1D1D1F"
        )
        self.label_name.place(relx=0.06, rely=0.15, anchor="w")

        ctk.CTkLabel(
            self,
            text="Статистика предмета",
            font=("Segoe UI Semibold", 13),
            text_color="#86868B"
        ).place(relx=0.06, rely=0.22, anchor="w")

        # инфо блоки
        self.info1 = ctk.CTkFrame(
            self,
            fg_color="#F5F5F7",
            corner_radius=19,
            width=350,
            height=75
        )
        self.info1.place(relx=0.5, rely=0.34, anchor="center")

        ctk.CTkLabel(
            self.info1,
            text="ОБЩЕЕ ВРЕМЯ",
            font=("Segoe UI Bold", 11),
            text_color="#86868B"
        ).place(relx=0.05, rely=0.15, anchor="nw")

        self.total_time = ctk.CTkLabel(
            self.info1,
            text="",
            font=("Segoe UI Semibold", 25),
            text_color="#1D1D1F"
        )
        self.total_time.place(relx=0.05, rely=0.45, anchor="nw")

        self.info2 = ctk.CTkFrame(
            self,
            fg_color="#F5F5F7",
            corner_radius=19,
            width=350,
            height=75
        )
        self.info2.place(relx=0.5, rely=0.51, anchor="center")

        ctk.CTkLabel(
            self.info2,
            text="ВСЕГО ДНЕЙ",
            font=("Segoe UI Bold", 11),
            text_color="#86868B"
        ).place(relx=0.05, rely=0.15, anchor="nw")

        self.total_days = ctk.CTkLabel(
            self.info2,
            text="",
            font=("Segoe UI Semibold", 25),
            text_color="#1D1D1F"
        )
        self.total_days.place(relx=0.05, rely=0.45, anchor="nw")

        self.info3 = ctk.CTkFrame(
            self,
            fg_color="#F5F5F7",
            corner_radius=19,
            width=350,
            height=75
        )
        self.info3.place(relx=0.5, rely=0.68, anchor="center")

        ctk.CTkLabel(
            self.info3,
            text="СРЕДНЕЕ ВРЕМЯ В ДЕНЬ",
            font=("Segoe UI Bold", 11),
            text_color="#86868B"
        ).place(relx=0.05, rely=0.15, anchor="nw")

        self.avg_time_sessions = ctk.CTkLabel(
            self.info3,
            text="",
            font=("Segoe UI Semibold", 25),
            text_color="#1D1D1F"
        )
        self.avg_time_sessions.place(relx=0.05, rely=0.45, anchor="nw")

        # кнопки управления
        arrow_img = ctk.CTkImage(
            light_image=Image.open(self.pm.file_path("assets", "icons", "icon_back.png")),
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

        self.btn_date_range = ctk.CTkButton(
            self,
            text="Выбрать период",
            font=("Segoe UI Semibold", 15),
            text_color="#1D1D1F",
            fg_color="#D3E3FD",
            hover_color="#C1D5F0",
            corner_radius=29,
            width=350,
            height=58,
            command=self.open_date_range_window
        )
        self.btn_date_range.place(relx=0.5, rely=0.88, anchor="center")

    def back(self) -> None:
        self.controller.show_frame("SubjectActions")

    def on_show(self) -> None:
        """
        Обновляет информацию при показе страницы.
        """
        name = self.controller.current_subject
        if name:
            has_history = self.controller.is_history(name)
            self.btn_date_range.configure(state="normal" if has_history else "disabled")

            self.label_name.configure(text=name.upper())
            self.total_time.configure(
                text=self.controller.get_total_time(name))
            self.total_days.configure(
                text=self.controller.get_total_days(name))
            self.avg_time_sessions.configure(
                text=self.controller.get_avg_study_time(name))

    def update_ui(self, new_data: dict, subject: str) -> None:
        """
        Обновляет информацию в инфо блоках после выбора периода.
        :param new_data: Отфильтрованные данные истории предмета.
        :param subject: Предмет.
        """
        self.total_time.configure(
            text=self.controller.get_total_time(subject, new_data)
        )
        self.total_days.configure(
            text=self.controller.get_total_days(subject, new_data)
        )
        self.avg_time_sessions.configure(
            text=self.controller.get_avg_study_time(subject, new_data)
        )

    def open_date_range_window(self) -> None:
        """Открывает окно выбора периода."""
        ask_date_range(self.controller, self.update_ui)
