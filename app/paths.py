import sys
import os
from pathlib import Path


class PathManager:
    def __init__(self, app_name: str):
        self.app_name = app_name
        self.is_frozen = hasattr(sys, "_MEIPASS")

        if self.is_frozen:
            self.base_path = Path(sys._MEIPASS)
        else:
            self.base_path = Path(__file__).resolve().parent

    def file_path(self, *args: str) -> Path:
        """
        Определяет правильный путь к файлам.
        :param args: Строки, элементы пути.
        :return: Корректный путь к файлу.
        """
        return self.base_path.joinpath(*args)

    def get_data_path(self, data_base: str) -> str:
        """
        Определяет путь к базе данных в зависимости от среды.
        :param data_base: База по умолчанию.
        :return: Путь к базе данных.
        """
        if self.is_frozen:
            app_dir = Path(os.getenv("LOCALAPPDATA")) / self.app_name
            app_dir.mkdir(parents=True, exist_ok=True)
            data_path = app_dir / "data.json"
            if not data_path.exists():
                data = self.file_path(data_base)
                data_path.write_text(data.read_text(encoding="utf-8"), encoding="utf-8")
            return str(data_path)

        return str(self.file_path(data_base))
