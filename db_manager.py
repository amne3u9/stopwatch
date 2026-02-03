import json


class DataBaseManager:

    def load_base(self) -> dict:
        """
        Считывает базу из файла(data_base.json).
        :return: Словарь.
        """
        with open("data_base.json", "r", encoding="utf-8") as db:
            return json.load(db)

    def is_subject_in_db(self, subject: str, data: dict) -> bool:
        """
        Проверяет наличие предмета(subject) в полученных данных(data).
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
