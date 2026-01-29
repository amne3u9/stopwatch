import time


class Stopwatch:
    """
    Секундомер, фиксирует время.

    Атрибуты:
        start_time(float): начало отсчета.
        total_t(float): срез времени.
        running(bool): флаг вкл./выкл.
    """

    def __init__(self):
        """Инициализирует атрибуты секундомера."""
        self.start_time: float = 0.0
        self.total_t: float = 0.0
        self.running: bool = False

    def start_t(self) -> None:
        """
        Фиксирует начало отсчета.
        Переводит флаг в True.
        """
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def stop_t(self) -> None:
        """
        Считает накопившиеся время, добавляет в total_t.
        Переводит флаг в False.
        """
        if self.running:
            self.total_t += (time.time() - self.start_time)
            self.running = False

    def reset_t(self) -> float:
        """
        Считает накопившееся время, добавляет в total_t.
        Форматирует значение, подготавливает к отправке.
        Переводит флаг в False.
        Очищает значение total_t.
        :return: Общее количество секунд, накопленных в total_t.
        """
        if self.running:
            self.total_t += (time.time() - self.start_time)

        duration = round(self.total_t, 2)
        self.running = False
        self.total_t = 0.0

        return duration

    def get_t(self) -> time.struct_time:
        """
        :return: Именованный кортеж struct_time.
        """
        if self.running:
            return time.gmtime(self.total_t + (time.time() - self.start_time))
        return time.gmtime(self.total_t)
