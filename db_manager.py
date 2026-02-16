import json
from datetime import datetime, date


class DataBaseManager:
    """
    Менеджер базы данных на основе JSON,
    отвечает за чтение/запись и операции над предметами
    и их историей сессий.
    """

    def load_base(self) -> dict:
        """
        Считывает базу из файла.
        :return: Словарь.
        """
        with open("data_base.json", "r", encoding="utf-8") as db:
            return json.load(db)

    def is_subject_in_db(self, subject: str, data: dict) -> bool:
        """
        Проверяет наличие предмета в полученных данных.
        :param subject: Название предмета.
        :param data: Данные из базы.
        :return: Bool значение.
        """
        return subject in data["subjects"]

    def save_data(self, data: dict) -> None:
        """
        Сохраняет новые данные в файл.
        :param data: Словарь.
        """
        with open("data_base.json", "w", encoding="utf-8") as db:
            json.dump(data, db, indent=4, ensure_ascii=False)

    def add_subject(self, name: str) -> bool:
        """
        Добавляет предмет(name).
        :param name: Предмет.
        :return: Bool значение.
        """
        # считываем базу из файла
        base = self.load_base()
        # проверяем отсутствие предмета в базе
        if self.is_subject_in_db(name, base):
            return False
        # добавляем новый предмет(name) в "subjects" со значением "history".
        base["subjects"][name] = {"history": {}}
        # обновляем базу
        self.save_data(base)
        return True

    def delete_subject(self, name: str) -> None:
        """
        Удаляет предмет(name).
        :param name: Предмет.
        """
        # считываем базу из файла
        base = self.load_base()
        # удаляем предмет(name) из "subjects"
        del base["subjects"][name]
        # обновляем базу
        self.save_data(base)

    def get_subjects(self) -> list[str]:
        """
        :return: Список предметов из базы.
        """
        return list(self.load_base()["subjects"].keys())

    def add_session(self, name: str, duration: float) -> None:
        """
        Добавляет временную сессию по дате в предмет.
        :param name: Предмет.
        :param duration: Время сессии.
        """
        # фиксируем дату сессии
        today = date.today().strftime('%Y-%m-%d')
        # считываем базу из файла
        base = self.load_base()
        # проверяем дату в истории, если нет создает список и добавляем время
        base["subjects"][name]["history"].setdefault(today, []).append(duration)
        # обновляем базу
        self.save_data(base)

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
        :return: Строку в формате "ЧЧ h. ММ m. СС s.".
        """
        q_hours = int(seconds // 3600)
        q_minutes = int((seconds % 3600) // 60)
        q_seconds = int(seconds % 60)

        return f"{q_hours:02} h. {q_minutes:02} m. {q_seconds:02} s."

    def get_total_time(self, data: dict, name: str) -> str:
        """
        :param data: Словарь с данными из базы.
        :param name: Предмет.
        :return: Строку, общего времени сессий предмета, в формате "ЧЧ h. ММ m. СС s.".
        """
        seconds = self.get_sum_seconds(data, name)
        result = self.format_seconds(seconds)

        return result

    def get_total_days(self, data: dict, name: str) -> int:
        """
        Считает кол-во дней предмета.
        :param data: Словарь с данными из базы.
        :param name: Предмет.
        :return: Число дней.
        """
        # получаем все даты предмета
        total_days = len(data["subjects"][name]["history"].keys())

        return total_days

    def get_avg_time_session(self, data: dict, name: str) -> str:
        """
        Считает среднее время сессии предмета.
        :param data: Словарь с данными из базы.
        :param name: Предмет.
        :return: Строку в формате "ЧЧ h. ММ m. СС s.".
        """
        # получаем кол-во дней
        quantity_days = self.get_total_days(data, name)
        if quantity_days == 0:
            return "00 h. 00 m. 00 s."
        # получаем кол-во секунд
        quantity_seconds = self.get_sum_seconds(data, name)
        # вычисляем среднее значение в секундах
        avg_seconds = quantity_seconds / quantity_days
        # получаем отформатированный результат
        result = self.format_seconds(avg_seconds)

        return result

    def get_start_date_datetime(self, data: dict, name: str) -> datetime.date:
        """
        Форматирует строку с начальной датой в datetime.date.

        :param data: Словарь с данными.
        :param name: Предмет.
        :return: Значение datetime.date формата.
        """
        start_date = self.get_min_date(data, name)
        return datetime.strptime(start_date, '%Y-%m-%d').date()

    def get_finish_date_datetime(self, data: dict, name: str) -> datetime.date:
        """
        Форматирует строку конечной датой в datetime.date.

        :param data: Словарь с данными.
        :param name: Предмет.
        :return: Значение datetime.date формата.
        """
        finish_date = self.get_max_date(data, name)
        return datetime.strptime(finish_date, '%Y-%m-%d').date()

    def get_min_date(self, data: dict, name: str) -> str:
        """
        Возвращает минимальную (раннюю) дату истории предмета.

        :param data: Словарь с данными.
        :param name: Предмет.
        :return: Строку начальной (ранней) даты истории предмета.
        """
        return min(data["subjects"][name]["history"])

    def get_max_date(self, data: dict, name: str) -> str:
        """
        Возвращает максимальную (позднюю) дату истории предмета.

        :param data: Словарь с данными.
        :param name: Предмет.
        :return: Строку максимальной (поздней) даты истории предмета.
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

    def is_date_order_correct(self, data: dict, date_from: str, date_to: str) -> bool:
        """
        Проверяет корректность порядка дат.

        :param data: Словарь с данными.
        :param date_from: Дата начала диапазона.
        :param date_to: Дата окончания диапазона.
        :return: Bool значение.
        """
        return date_from <= date_to

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
        filtered_dict = {"subjects":
                             {name:
                                  {"history":
                                       {}
                                   }
                              }
                         }
        filtered_dict["subjects"][name]["history"] = {date_: value for date_, value in
                                                      data["subjects"][name]["history"].items() if
                                                      date_from <= date_ <= date_to}

        return filtered_dict
