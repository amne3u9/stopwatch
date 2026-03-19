import customtkinter as ctk

from utils import center_window
from db_manager import DataBaseManager
from gui_subject_manager import StartWork
from subject_menu import SubjectActions
from gui_history import History
from gui_stopwatch import StopwatchWindow


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        center_window(self, 400, 500)
        self.title("Subject Selection")
        self.configure(fg_color="#FFFFFF")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.general_closure)

        self.stopwatch_window: StopwatchWindow | None = None
        self.subject_in_stopwatch = None

        self.db_path = "demo_data.json"
        self.db_m = DataBaseManager(self.db_path)
        self.data = self.load_data()
        self.current_subject = ""

        self.frames: dict[str, ctk.CTkFrame] = {}

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        for F in (StartWork, SubjectActions, History):
            page_name = F.__name__
            frame = F(master=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartWork")

    def open_stopwatch(self) -> None:
        """
        Открывает окно секундомера.
        Если окно уже существует — переносит его на передний план.
        """
        if self.stopwatch_window is None:
            self.subject_in_stopwatch = self.current_subject
            self.stopwatch_window = StopwatchWindow(self, self.subject_in_stopwatch)
        else:
            self.stopwatch_window.focus()
            self.stopwatch_window.lift()

    def stopwatch_status(self) -> bool:
        return self.stopwatch_window.stop_work()

    def close_stopwatch_window(self) -> None:
        self.stopwatch_window.destroy()
        self.stopwatch_closed()

    def stopwatch_closed(self) -> None:
        """Сбрасывает ссылку на окно секундомера после его закрытия."""
        self.stopwatch_window = None
        self.subject_in_stopwatch = None

    def load_data(self) -> dict:
        return self.db_m.load_base()

    def save_data(self, data: dict) -> None:
        self.db_m.save_data(data)

    def add_subject(self, subject: str) -> bool:
        if self.db_m.is_subject_in_db(self.data, subject):
            return False
        self.data = self.db_m.add_subject(self.data, subject)
        self.save_data(self.data)
        return True

    def is_stopwatch_participation(self, subject: str) -> bool:
        if subject == self.subject_in_stopwatch:
            return self.stopwatch_status()
        return False

    def delete_subject(self, subject: str, close_swatch: bool) -> None:
        if close_swatch:
            self.close_stopwatch_window()
        self.data = self.db_m.delete_subject(self.data, subject)
        self.save_data(self.data)

    def is_subject_in_db(self, subject: str) -> bool:
        return self.db_m.is_subject_in_db(self.data, subject)

    def get_subjects(self) -> list[str]:
        return self.db_m.get_subjects(self.data)

    def add_session(self, subject: str, value: float, session_date: str) -> None:
        self.data = self.db_m.add_session(self.data, subject, value, session_date)
        self.save_data(self.data)

    def get_time(self, subject: str) -> str:
        return self.db_m.get_time(self.data, subject)

    def is_history(self, subject: str) -> bool:
        return bool(self.data["subjects"][subject]["history"])

    def get_total_time(self, subject: str, data: dict | None = None) -> str:
        if data is None:
            return self.db_m.get_total_time(self.data, subject)
        return self.db_m.get_total_time(data, subject)

    def get_total_days(self, subject: str, data: dict | None = None) -> int:
        if data is None:
            return self.db_m.get_total_days(self.data, subject)
        return self.db_m.get_total_days(data, subject)

    def get_avg_study_time(self, subject: str, data: dict | None = None) -> str:
        if data is None:
            return self.db_m.get_avg_study_time(self.data, subject)
        return self.db_m.get_avg_study_time(data, subject)

    def get_start_date(self) -> str:
        return self.db_m.get_min_date(self.data, self.current_subject)

    def get_end_date(self) -> str:
        return self.db_m.get_max_date(self.data, self.current_subject)

    def get_data_filter(self, date_from: str, date_to: str) -> dict:
        return self.db_m.get_data_filter(self.data, self.current_subject, date_from, date_to)

    def set_current_subject(self, name: str) -> None:
        self.current_subject = name

    def show_frame(self, page_name: str) -> None:
        frame = self.frames[page_name]
        frame.tkraise()

        if hasattr(frame, "on_show"):
            frame.on_show()

        self.title(getattr(frame, "window_title", "Subject Selection"))

    def general_closure(self) -> None:
        """
        Перехватывает закрытие приложения.
        Если секундомер открыт — запускает проверку закрытия секундомера.
        """
        if self.stopwatch_window is not None:
            self.stopwatch_window.closing_check(True)
        else:
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
