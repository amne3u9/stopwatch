class SubjectsManager:
    """
    Менеджер предметов.
    Хранит список доступных предметов и управляет добавлением/удалением.

    Атрибуты:
        subjects(list): Список предметов.
    """

    def __init__(self, start_subjects: list[str] | None = None):
        """Инициализирует атрибуты Менеджера предметов"""
        self.subjects: list = start_subjects or []

    def add_subject(self, name: str) -> bool:
        """
        Добавляет предмет, если его нет.
        :param name: Название предмета.
        :return: Bool значение.
        """
        if name not in self.subjects:
            self.subjects.append(name)
            return True
        else:
            return False

    def delete_subject(self, name: str) -> bool:
        """
        Удаляет предмет если он есть.
        :param name: Название предмета.
        :return: Bool значение.
        """
        if name in self.subjects:
            self.subjects.remove(name)
            return True
        else:
            return False

    def get_subjects(self) -> list:
        """
        :return: Список с предметами.
        """
        return self.subjects
