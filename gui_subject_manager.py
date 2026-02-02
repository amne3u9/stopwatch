"""Окно выбора предмета"""
from tkinter import *
from tkinter import ttk
from utils import center_window
from db_manager import DataBaseManager
from subject_menu import creation_menu_subject

# ---- Логика ----
db_m = DataBaseManager()


def choice() -> None:
    """
    Проверяет выбор предмета.
    Показывает сообщение.
    """
    name_subject = combo_menu.get()
    if name_subject:
        shell_SS.withdraw()
        creation_menu_subject(shell_SS, name_subject)
    else:
        label.config(text="Выберите предмет из списка", fg="dark red")


def add() -> None:
    """
    Открывает окно для добавления нового предмета.
    Проверяет ввод, добавляет предмет в список(combo_menu['values']).
    Показывает сообщение.
    """

    def add_new_value() -> None:
        new_subject = subject.get().strip()
        if new_subject:
            passage = db_m.add_subject(new_subject)
            if passage:
                update_subjects = db_m.get_subjects()
                combo_menu.config(values=update_subjects)
                label.config(text="Предмет добавлен", fg='green')
                new_window.destroy()
            else:
                label2.config(text="Такой предмет уже есть", fg='dark red')
        else:
            label2.config(text="Напишите название предмета", fg='dark red')

    new_window = Toplevel(shell_SS)
    new_window.title('New Subject')
    center_window(new_window, 250, 150)
    new_window.resizable(False, False)
    label2 = Label(new_window, text="Название нового предмета")
    label2.place(relx=0.5, rely=0.1, anchor='center')

    # окно ввода
    subject = ttk.Entry(new_window)
    subject.place(relx=0.5, rely=0.3, anchor='center')

    # кнопки
    btn_ok = ttk.Button(new_window, text="OK", command=add_new_value)
    btn_ok.pack(expand=True, anchor='s', pady=30)


def delete() -> None:
    """
    Обновляет список(combo_menu['values']).
    Показывает сообщение.
    """

    def deletion_subject() -> None:
        db_m.delete_subject(del_value)
        update_subjects = db_m.get_subjects()
        combo_menu.config(values=update_subjects)
        combo_menu.set("")
        label.config(text="Предмет удален", fg='green')
        new_window.destroy()

    del_value = combo_menu.get()
    if del_value:
        if del_value in db_m.get_subjects():
            new_window = Toplevel(shell_SS)
            new_window.title('Deletion')
            center_window(new_window, 250, 150)
            new_window.resizable(False, False)
            label2 = Label(new_window, text=f"Удаляем {del_value} и очистить историю?")
            label2.place(relx=0.5, rely=0.1, anchor='center')

            btn_ok = ttk.Button(new_window, text="OK", command=deletion_subject)
            btn_ok.pack(expand=True, anchor='s', pady=30)
        else:
            label.config(text="Такого предмета нет", fg="dark red")
    else:
        label.config(text="Нечего удалять", fg="dark red")


# ---- GUI ----
shell_SS = Tk()
shell_SS.title('Subject Selection')
center_window(shell_SS, 300, 200)
shell_SS.resizable(False, False)
label = Label(shell_SS, text="Выберите предмет или создайте новый")
label.place(relx=0.5, rely=0.1, anchor='n')

# Кнопки управления
btn_choice = ttk.Button(shell_SS, text='Choice', command=choice)
btn_add = ttk.Button(shell_SS, text='Add', command=add)
btn_delete = ttk.Button(shell_SS, text='Delete', command=delete)

# выпадающее меню
combo_menu = ttk.Combobox(shell_SS, values=db_m.get_subjects(), state="readonly")
combo_menu.pack(pady=45)

# Отображение кнопок
btn_choice.place(relx=0.5, rely=0.45, anchor='center')
btn_add.place(relx=0.1, rely=0.9, anchor='sw')
btn_delete.place(relx=0.9, rely=0.9, anchor='se')

# Запуск окна
shell_SS.mainloop()
