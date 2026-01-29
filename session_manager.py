from datetime import date


class SessionManager:
    """
    Менеджер временных сессий.

    Атрибуты:
        sessions(dict): Словарь для хранения сессий.
    """

    def __init__(self):
        """Инициализирует атрибуты менеджера сессий."""
        self.sessions: dict[str, list[float]] = {}

    def add_session(self, duration: float) -> None:
        """
        Фиксирует актуальную дату, форматирует в строку.
        Формирует ключ, добавляет duration в sessions.
        :param duration: Количество секунд.
        :return: None.
        """
        today = date.today().strftime('%Y-%m-%d')
        if today in self.sessions:
            self.sessions[today].append(duration)
        else:
            self.sessions[today] = [duration]

    def get_sessions_by_date(self, date_: str) -> list[float]:
        """
        :param date_: Дата, ключ для sessions.
        :return: Список сессий под ключом date_.
        """
        return self.sessions[date_]

    def get_total_by_date(self, date_: str) -> float:
        """
        :param date_: Дата, ключ для sessions.
        :return: Сумму секунд под ключом date_.
        """
        return sum(self.get_sessions_by_date(date_))
