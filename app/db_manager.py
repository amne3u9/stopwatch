import json
from datetime import date


class DataBaseManager:
    """
    Менеджер базы данных на основе JSON,
    отвечает за чтение/запись и операции над предметами
    и их историей сессий.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_base(self) -> dict:
        """
        Считывает базу из файла.
        :return: Словарь с данными.
        """
        with open(self.file_path, "r", encoding="utf-8") as db:
            return json.load(db)

    def is_subject_in_db(self, data: dict, subject: str) -> bool:
        """
        Проверяет наличие предмета в полученных данных.
        :param data: Словарь с данными.
        :param subject: Название предмета.
        :return: Bool значение.
        """
        return subject in data["subjects"]

    def save_data(self, data: dict) -> None:
        """
        Сохраняет новые данные в файл.
        :param data: Словарь с данными.
        """
        with open(self.file_path, "w", encoding="utf-8") as db:
            json.dump(data, db, indent=4, ensure_ascii=False)

    def add_subject(self, data: dict, name: str) -> dict:
        """
        Добавляет новый предмет в данные.
        :param data: Словарь с данными.
        :param name: Предмет.
        :return: Словарь с добавленным предметом.
        """
        # добавляем новый предмет(name) в "subjects" со значением "history".
        data["subjects"][name] = {"history": {}}

        return data

    def delete_subject(self, data: dict, name: str) -> dict:
        """
        Удаляет предмет из данных.
        :param data: Словарь с данными.
        :param name: Предмет.
        :return: Словарь без удаленного предмета.
        """
        # удаляем предмет(name) из "subjects"
        del data["subjects"][name]

        return data

    def get_subjects(self, data: dict) -> list[str]:
        """
        :param data: Словарь с данными.
        :return: Список предметов из словаря.
        """
        return list(data["subjects"].keys())

    def get_date_today(self) -> str:
        return date.today().strftime('%Y-%m-%d')

    def is_today_in_subject(self, data: dict, today: str, name: str) -> bool:
        return today in data["subjects"][name]["history"]

    def get_sum_seconds_today(self, sessions: list[float]) -> float:
        return sum(sessions)

    def get_time(self, data: dict, name: str) -> str:
        today = self.get_date_today()
        if self.is_today_in_subject(data, today, name):
            data_today = data["subjects"][name]["history"][today]
            return self.format_seconds(self.get_sum_seconds_today(data_today))
        else:
            return "00 ч. 00 м. 00 с."

    def add_session(self, data: dict, name: str, duration: float, session_date: str) -> dict:
        """
        Добавляет новую сессию по дате в предмет.
        :param data: Словарь с данными.
        :param name: Предмет.
        :param duration: Время сессии.
        :param session_date: Дата запуска секундомера.
        :return: Словарь с добавленной сессией.
        """
        # проверяем дату в истории, если нет создает список и добавляем время
        data["subjects"][name]["history"].setdefault(session_date, []).append(duration)

        return data

    def get_sum_seconds(self, data: dict, name: str) -> float:
        """
        Считает общее время сессий предмета в секундах.
        :param data: Словарь с данными из базы.
        :param name: Предмет
        :return: Общее число секунд.
        """
        # получаем сессии по дням
        days = data["subjects"][name]["history"].values()
        # суммируем сессии
        sum_seconds = sum(sum(day) for day in days)

        return sum_seconds

    def format_seconds(self, seconds: float) -> str:
        """
        Форматирует число секунд в ЧЧ.ММ.СС.
        :param seconds: Число секунд.
        :return: Строку в формате "ЧЧ ч. ММ м. СС с.".
        """
        q_hours = int(seconds // 3600)
        q_minutes = int((seconds % 3600) // 60)
        q_seconds = int(seconds % 60)

        return f"{q_hours:02} ч. {q_minutes:02} м. {q_seconds:02} с."

    def get_total_time(self, data: dict, name: str) -> str:
        """
        :param data: Словарь с данными.
        :param name: Предмет.
        :return: Строку, общего времени сессий предмета, в формате "ЧЧ ч. ММ м. СС с.".
        """
        seconds = self.get_sum_seconds(data, name)
        result = self.format_seconds(seconds)

        return result

    def get_total_days(self, data: dict, name: str) -> int:
        """
        Считает кол-во дней предмета.
        :param data: Словарь с данными.
        :param name: Предмет.
        :return: Число дней.
        """
        # получаем все даты предмета
        total_days = len(data["subjects"][name]["history"].keys())

        return total_days

    def get_avg_study_time(self, data: dict, name: str) -> str:
        """
        Считает среднее время сессии предмета по дням.
        :param data: Словарь с данными.
        :param name: Предмет.
        :return: Строку в формате "ЧЧ ч. ММ м. СС с.".
        """
        # получаем кол-во дней
        quantity_days = self.get_total_days(data, name)
        if quantity_days == 0:
            return "00 ч. 00 м. 00 с."
        # получаем кол-во секунд
        quantity_seconds = self.get_sum_seconds(data, name)
        # вычисляем среднее значение в секундах
        avg_seconds = quantity_seconds / quantity_days
        # получаем отформатированный результат
        result = self.format_seconds(avg_seconds)

        return result

    def get_min_date(self, data: dict, name: str) -> str:
        """
        Возвращает минимальную (раннюю) дату истории предмета.
        :param data: Словарь с данными.
        :param name: Предмет.
        :return: Начальную (раннюю) дату истории предмета.
        """
        return min(data["subjects"][name]["history"])

    def get_max_date(self, data: dict, name: str) -> str:
        """
        Возвращает максимальную (позднюю) дату истории предмета.
        :param data: Словарь с данными.
        :param name: Предмет.
        :return: Максимальную (позднюю) дату истории предмета.
        """
        return max(data["subjects"][name]["history"])

    def is_date_in_history(self, data: dict, name: str, date_: str) -> bool:
        """
        Проверяет корректность даты.

        :param data: Словарь с данными.
        :param name: Предмет.
        :param date_: Строка даты.
        :return: Bool значение.
        """
        return date_ in data["subjects"][name]["history"]

    def get_data_filter(self, data: dict, name: str, date_from=None, date_to=None) -> dict:
        """
        Фильтрует историю предмета по диапазону дат.

        :param data: Словарь с данными.
        :param name: Предмет.
        :param date_from: Дата начала.
        :param date_to: Дата окончания.
        :return: Словарь с историей предмета за указанный период или строка с ошибкой.
        """
        if date_from is None:
            date_from = self.get_min_date(data, name)
        if date_to is None:
            date_to = self.get_max_date(data, name)
        filtered_dict = {
            "subjects":
                {name:
                     {"history":
                          {}
                      }
                 }
        }
        filtered_dict["subjects"][name]["history"] = {
            date_: value for date_, value
            in data["subjects"][name]["history"].items()
            if date_from <= date_ <= date_to
        }

        return filtered_dict
