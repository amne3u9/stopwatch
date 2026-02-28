import customtkinter as ctk

from utils import center_window
from db_manager import DataBaseManager
from gui_subject_manager import StartWork
from subject_menu import SubjectActions
from gui_history import History


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        center_window(self, 400, 500)
        self.title('Subject Selection')
        self.configure(fg_color='#FFFFFF')
        self.resizable(False, False)

        self.db_path = "demo_data.json"
        self.db_m = DataBaseManager(self.db_path)
        self.data = self.load_data()
        self.current_subject = ""

        self.frames = {}

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        for F in (StartWork, SubjectActions, History):
            page_name = F.__name__
            frame = F(master=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartWork")

    def load_data(self) -> dict:
        return self.db_m.load_base()

    def save_data(self, data: dict) -> None:
        self.db_m.save_data(data)

    def add_subject(self, subject) -> bool:
        if self.db_m.is_subject_in_db(self.data, subject):
            return False
        self.data = self.db_m.add_subject(self.data, subject)
        self.save_data(self.data)
        return True

    def delete_subject(self, subject) -> None:
        self.data = self.db_m.delete_subject(self.data, subject)
        self.save_data(self.data)

    def is_subject_in_db(self, subject) -> bool:
        return self.db_m.is_subject_in_db(self.data, subject)

    def get_subjects(self) -> list:
        return self.db_m.get_subjects(self.data)

    def add_session(self, subject, value) -> None:
        self.data = self.db_m.add_session(self.data, subject, value)
        self.save_data(self.data)

    def get_time(self, subject) -> str:
        return self.db_m.get_time(self.data, subject)

    def is_history(self, subject) -> bool:
        return bool(self.data["subjects"][subject]["history"])

    def get_total_time(self, subject, data=None) -> str:
        if data is None:
            return self.db_m.get_total_time(self.data, subject)
        return self.db_m.get_total_time(data, subject)

    def get_total_days(self, subject, data=None) -> int:
        if data is None:
            return self.db_m.get_total_days(self.data, subject)
        return self.db_m.get_total_days(data, subject)

    def get_avg_study_time(self, subject, data=None) -> str:
        if data is None:
            return self.db_m.get_avg_study_time(self.data, subject)
        return self.db_m.get_avg_study_time(data, subject)

    def get_start_date(self):
        return self.db_m.get_min_date(self.data, self.current_subject)

    def get_end_date(self):
        return self.db_m.get_max_date(self.data, self.current_subject)

    def get_data_filter(self, date_from, date_to) -> dict:
        return self.db_m.get_data_filter(self.data, self.current_subject, date_from, date_to)

    def set_current_subject(self, name):
        self.current_subject = name

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

        if hasattr(frame, "on_show"):
            frame.on_show()

        self.title(getattr(frame, "window_title", "Subject Selection"))


if __name__ == "__main__":
    app = App()
    app.mainloop()
