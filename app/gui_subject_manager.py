"""Окно выбора предмета"""
import customtkinter as ctk
from customtkinter import CTkToplevel

from utils import extra_window


class StartWork(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color="transparent")

        self.label = ctk.CTkLabel(
            self,
            text="Выберите предмет из списка",
            font=("Segoe UI Semibold", 14),
            text_color="#86868B"
        )
        self.label.place(relx=0.5, rely=0.17, anchor="n")

        # выпадающее меню
        self.combo_menu = ctk.CTkComboBox(
            self,
            values=self.controller.get_subjects(),
            font=("Segoe UI", 14),
            text_color="#1D1D1F",
            border_width=0,
            border_color="#E5E5E7",
            fg_color="#F5F5F7",
            dropdown_fg_color="#FFFFFF",
            dropdown_hover_color="#F5F5F7",
            button_color="#D3E3FD",
            corner_radius=12,
            width=300,
            height=50,
            state="readonly"
        )
        self.combo_menu.place(relx=0.5, rely=0.37, anchor="center")

        # Кнопки управления
        self.btn_choice = ctk.CTkButton(
            self,
            text="Выбрать",
            font=("Segoe UI Semibold", 14),
            text_color="#1D1D1F",
            fg_color="#D3E3FD",
            hover_color="#C1D5F0",
            corner_radius=25,
            width=300,
            height=50,
            command=self.choice
        )
        self.btn_choice.place(relx=0.5, rely=0.58, anchor="center")

        self.btn_add = ctk.CTkButton(
            self,
            text="Добавить новый",
            font=("Segoe UI Semibold", 14),
            text_color="#1D1D1F",
            fg_color="#F5F5F7",
            hover_color="#E5E5E7",
            corner_radius=25,
            width=300,
            height=50,
            command=self.add
        )
        self.btn_add.place(relx=0.5, rely=0.70, anchor="center")

        self.btn_delete = ctk.CTkButton(
            self,
            text="Удалить предмет",
            font=("Segoe UI Semibold", 14),
            text_color="#BA1A1A",
            fg_color="transparent",
            hover_color="#FFDAD6",
            corner_radius=25,
            width=300,
            height=50,
            command=self.delete
        )
        self.btn_delete.place(relx=0.5, rely=0.85, anchor="center")

    def return_label(self) -> None:
        """Возвращает текст заголовка."""
        self.label.configure(
            text="Выберите предмет из списка",
            text_color="#86868B"
        )

    def choice(self) -> None:
        """
        Проверяет выбор предмета.
        Показывает сообщение.
        """
        name_subject = self.combo_menu.get()
        if name_subject:
            self.controller.set_current_subject(name_subject)
            self.controller.show_frame("SubjectActions")
        else:
            self.label.configure(text="Выберите предмет из списка или добавьте новый", text_color="#007AFF")
            self.after(5000, self.return_label)

    def add(self) -> None:
        """Создает окно для добавления нового предмета."""

        def return_label_new_name() -> None:
            """Возвращает текст окна добавления нового предмета."""
            label_new_name.configure(
                text="Введите имя предмета",
                text_color="#1D1D1F"
            )

        def add_new_value() -> None:
            """
            Передает имя предмета для добавления в базу данных.
            Показывает сообщение.
            """
            new_subject = window_entry.get().strip()
            if new_subject:
                passage = self.controller.add_subject(new_subject)
                if passage:
                    update_subjects = self.controller.get_subjects()
                    self.combo_menu.configure(values=update_subjects)
                    self.label.configure(text="Предмет добавлен", text_color="#007AFF")
                    new_window.destroy()
                    self.after(3500, self.return_label)
                else:
                    label_new_name.configure(text="Такой предмет уже есть", text_color="#007AFF")
                    new_window.after(3500, return_label_new_name)
            else:
                label_new_name.configure(text="Введите имя предмета", text_color="#007AFF")
                new_window.after(3500, return_label_new_name)

        def update_label_counter(*args) -> None:
            """
            Обновляет количество оставшихся вводимых символов.
            Обновляет цвет рамки окна ввода и текст label_counter.
            Ограничивает количество вводимых символов.
            """
            max_size = 25
            name = text.get()
            text_size = len(name)

            if text_size > max_size:
                text.set(name[:25])
                text_size = max_size

            remainder = max_size - text_size
            if 5 < remainder < 26:
                label_counter.configure(text=f"осталось символов: {remainder}",
                                        text_color="#86868B"
                                        )
                window_entry.configure(border_color="#86868B")
            elif 0 < remainder <= 5:
                label_counter.configure(text=f"осталось символов: {remainder}",
                                        text_color="#FF8C00"
                                        )
                window_entry.configure(border_color="#FF8C00")
            else:
                label_counter.configure(text=f"осталось символов: {remainder}",
                                        text_color="#EA4335")
                window_entry.configure(border_color="#EA4335"
                                       )

        new_window = CTkToplevel(self.controller)
        new_window.title("Новый предмет")
        extra_window(self.controller, new_window, 320, 240)
        new_window.resizable(False, False)
        new_window.configure(fg_color="#FFFFFF")
        new_window.grab_set()

        label_new_name = ctk.CTkLabel(
            new_window,
            text="Введите имя предмета",
            font=("Segoe UI Semibold", 13),
            text_color="#1D1D1F"
        )
        label_new_name.place(relx=0.5, rely=0.18, anchor="center")

        # отслеживаемая строка
        text = ctk.StringVar()
        # окно ввода
        window_entry = ctk.CTkEntry(
            new_window,
            font=("Segoe UI", 14),
            text_color="#1D1D1F",
            textvariable=text,
            border_width=1,
            border_color="#E5E5E7",
            fg_color="#F5F5F7",
            width=230,
            height=30,
            corner_radius=8
        )
        window_entry.place(relx=0.5, rely=0.4, anchor="center")
        # обработчик событий
        text.trace_add("write", update_label_counter)

        label_counter = ctk.CTkLabel(
            new_window,
            text="осталось символов: 25",
            font=("Segoe UI Semibold", 13),
            text_color="#86868B"
        )
        label_counter.place(relx=0.5, rely=0.53, anchor="center")

        # кнопки
        btn_ok = ctk.CTkButton(
            new_window,
            text="Добавить",
            font=("Segoe UI Semibold", 13),
            text_color="#1D1D1F",
            fg_color="#D3E3FD",
            hover_color="#C1D5F0",
            corner_radius=20,
            width=150,
            height=40,
            command=add_new_value
        )
        btn_ok.place(relx=0.5, rely=0.8, anchor="center")

    def delete(self) -> None:
        """
        Создает окно для удаления предмета.
        Показывает сообщение.
        """

        def deletion_subject(close_swatch: bool = False) -> None:
            """
            Передает имя предмета для удаления из базы данных.
            Показывает сообщение.
            """
            self.controller.delete_subject(del_value, close_swatch)
            update_subjects = self.controller.get_subjects()
            self.combo_menu.configure(values=update_subjects)
            self.combo_menu.set("")
            self.label.configure(text="Предмет удален", text_color="#007AFF")
            new_window.destroy()
            self.after(3500, self.return_label)

        del_value = self.combo_menu.get()
        if del_value:
            if del_value in self.controller.get_subjects():
                close_stopwatch = self.controller.is_stopwatch_participation(del_value)
                new_window = CTkToplevel(self.controller)
                new_window.title("Удаление предмета")
                extra_window(self.controller, new_window, 320, 240)
                new_window.configure(fg_color="#FFFFFF")
                new_window.resizable(False, False)
                new_window.grab_set()

                label2 = ctk.CTkLabel(
                    new_window,
                    text=f"",
                    font=("Segoe UI Semibold", 13),
                    text_color="#1D1D1F"
                )
                label2.place(relx=0.5, rely=0.35, anchor="center")

                if not close_stopwatch:
                    label2.configure(
                        text="Удалить предмет и очистить историю?"
                    )
                else:
                    label2.configure(
                        text="У этого предмета есть активный секундомер.\n Удалить предмет и очистить историю?"
                    )

                btn_ok = ctk.CTkButton(
                    new_window,
                    text="Удалить",
                    font=("Segoe UI Semibold", 13),
                    text_color="#1D1D1F",
                    fg_color="#D3E3FD",
                    hover_color="#C1D5F0",
                    corner_radius=20,
                    width=150,
                    height=40,
                    command=lambda: deletion_subject(close_stopwatch)
                )
                btn_ok.place(relx=0.5, rely=0.8, anchor="center")
            else:
                self.label.configure(text="Такого предмета нет", text_color="#007AFF")
        else:
            self.label.configure(text="Выберите предмет для удаления", text_color="#007AFF")
            self.after(5000, self.return_label)
