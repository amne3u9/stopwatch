"""Окно выбора предмета"""
import customtkinter as ctk
from customtkinter import CTkToplevel

from utils import extra_window


# ---- Логика ----

class StartWork(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure(fg_color="transparent")

        # ---- GUI ----

        self.label_main = ctk.CTkLabel(
            self,
            text="ВЫБОР ПРЕДМЕТА",
            font=("Segoe UI Semibold", 20),
            text_color='#1D1D1F'
        )
        self.label_main.place(relx=0.5, rely=0.10, anchor='n')

        self.label = ctk.CTkLabel(
            self,
            text="Выберите предмет из списка",
            font=("Segoe UI Semibold", 13),
            text_color='#86868B'
        )
        self.label.place(relx=0.5, rely=0.22, anchor='n')

        # выпадающее меню
        self.combo_menu = ctk.CTkComboBox(
            self,
            values=self.controller.get_subjects(),
            font=("Segoe UI", 14),
            text_color='#1D1D1F',
            border_width=1,
            border_color="#E5E5E7",
            fg_color='#F5F5F7',
            dropdown_fg_color='#FFFFFF',
            dropdown_hover_color='#F5F5F7',
            button_color='#D3E3FD',
            corner_radius=12,
            width=300,
            height=50,
            state="readonly"
        )
        self.combo_menu.place(relx=0.5, rely=0.37, anchor='center')

        # Кнопки управления
        self.btn_choice = ctk.CTkButton(
            self,
            text='Выбрать',
            font=("Segoe UI Semibold", 14),
            text_color='#1D1D1F',
            fg_color='#D3E3FD',
            hover_color="#C1D5F0",
            corner_radius=25,
            width=300,
            height=50,
            command=self.choice
        )
        self.btn_choice.place(relx=0.5, rely=0.55, anchor='center')

        self.btn_add = ctk.CTkButton(
            self,
            text='Добавить новый',
            font=("Segoe UI Semibold", 14),
            text_color='#1D1D1F',
            fg_color='#F5F5F7',
            hover_color="#E5E5E7",
            corner_radius=25,
            width=300,
            height=50,
            command=self.add
        )
        self.btn_add.place(relx=0.5, rely=0.63, anchor='n')

        self.btn_delete = ctk.CTkButton(
            self,
            text='Удалить предмет',
            font=("Segoe UI Semibold", 14),
            text_color="#BA1A1A",
            fg_color="transparent",
            hover_color="#FFDAD6",
            corner_radius=25,
            width=300,
            height=50,
            command=self.delete
        )
        self.btn_delete.place(relx=0.5, rely=0.90, anchor='center')

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
            self.label.configure(text="Выберите предмет из списка или добавьте новый", text_color='#007AFF')

    def add(self) -> None:
        """
        Открывает окно для добавления нового предмета.
        Проверяет ввод, добавляет предмет в список(combo_menu['values']).
        Показывает сообщение.
        """

        def add_new_value() -> None:
            new_subject = subject.get().strip()
            if new_subject:
                passage = self.controller.add_subject(new_subject)
                if passage:
                    update_subjects = self.controller.get_subjects()
                    self.combo_menu.configure(values=update_subjects)
                    self.label.configure(text="Предмет добавлен", text_color='#007AFF')
                    new_window.destroy()
                else:
                    label2.configure(text="Такой предмет уже есть", text_color='#007AFF')
            else:
                label2.configure(text="Введите имя предмета", text_color='#007AFF')

        new_window = CTkToplevel(self.controller)
        new_window.title('Новый предмет')
        extra_window(self.controller, new_window, 320, 240)
        new_window.resizable(False, False)
        new_window.configure(fg_color='#FFFFFF')
        new_window.grab_set()

        label2 = ctk.CTkLabel(
            new_window,
            text="Введите имя предмета",
            font=("Segoe UI Semibold", 13),
            text_color='#86868B'
        )
        label2.place(relx=0.5, rely=0.2, anchor='center')

        # окно ввода
        subject = ctk.CTkEntry(
            new_window,
            font=("Segoe UI", 14),
            text_color='#1D1D1F',
            border_width=1,
            border_color="#E5E5E7",
            fg_color='#F5F5F7',
            width=200,
            height=30,
            corner_radius=8
        )
        subject.place(relx=0.5, rely=0.4, anchor='center')

        # кнопки
        btn_ok = ctk.CTkButton(
            new_window,
            text="Добавить",
            font=("Segoe UI Semibold", 13),
            text_color='#1D1D1F',
            fg_color='#D3E3FD',
            hover_color="#C1D5F0",
            corner_radius=20,
            width=150,
            height=40,
            command=add_new_value
        )
        btn_ok.place(relx=0.5, rely=0.8, anchor='s')

    def delete(self) -> None:
        """
        Обновляет список(combo_menu['values']).
        Показывает сообщение.
        """

        def deletion_subject() -> None:
            self.controller.delete_subject(del_value)
            update_subjects = self.controller.get_subjects()
            self.combo_menu.configure(values=update_subjects)
            self.combo_menu.set("")
            self.label.configure(text="Предмет удален", text_color='#007AFF')
            new_window.destroy()

        del_value = self.combo_menu.get()
        if del_value:
            if del_value in self.controller.get_subjects():
                new_window = CTkToplevel(self.controller)
                new_window.title('Удаление предмета')
                extra_window(self.controller, new_window, 320, 240)
                new_window.configure(fg_color='#FFFFFF')
                new_window.resizable(False, False)
                new_window.grab_set()

                label2 = ctk.CTkLabel(
                    new_window,
                    text=f"Удалить предмет и очистить историю?",
                    font=("Segoe UI Semibold", 14),
                    text_color='#1D1D1F'
                )
                label2.place(relx=0.5, rely=0.30, anchor='center')

                btn_ok = ctk.CTkButton(
                    new_window,
                    text="Удалить",
                    font=("Segoe UI Semibold", 13),
                    text_color='#1D1D1F',
                    fg_color='#D3E3FD',
                    hover_color="#C1D5F0",
                    corner_radius=20,
                    width=150,
                    height=40,
                    command=deletion_subject
                )
                btn_ok.place(relx=0.5, rely=0.8, anchor='s')
            else:
                self.label.configure(text="Такого предмета нет", text_color='#007AFF')
        else:
            self.label.configure(text="Нечего удалять", text_color='#007AFF')
