# Трекер учебного времени

Настольное приложение для отслеживания времени, затраченного на изучение различных предметов.

Программа позволяет запускать и останавливать учебные сессии, сохранять историю занятий и анализировать затраченное
время.

Приложение написано на **Python** с использованием **CustomTkinter** для современного интерфейса.

---

## Интерфейс приложения

### Главное окно

![Стартовое окно](app/assets/screenshots/start_window.png)

### Секундомер

![Секундомер](app/assets/screenshots/stopwatch_window.png)

### История занятий

![История](app/assets/screenshots/history_window.png)

---

## Возможности

- запуск, остановка и сброс учебных сессий
- учёт времени по каждому предмету
- сохранение истории занятий в JSON
- просмотр истории и статистики
- фильтрация истории по диапазону дат
- обработка пользовательских сценариев (предупреждения, модальные окна)
- понятный и удобный графический интерфейс

---

## Используемые технологии

- Python 3.12
- customtkinter
- tkcalendar

---

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/amne3u9/stopwatch.git
```

2. Перейдите в папку проекта:

```
cd stopwatch
```

3. Установите зависимости:

```
pip install -r requirements.txt
```

---

## Запуск приложения

```
python app/main.py
```

---

## Структура проекта

```
stopwatch/
├── app/
│   ├── assets/
│   │   ├── icons/
│   │   │       icon_back.png
│   │   └── screenshots/
│   │       ├── history_window.png
│   │       ├── start_window.png
│   │       └── stopwatch_window.png 
│   │
│   ├── main.py
│   ├── db_manager.py
│   ├── demo_data.json
│   ├── gui_date_range_selection.py
│   ├── gui_history.py
│   ├── gui_stopwatch.py
│   ├── gui_subject_manager.py
│   ├── stopwatch.py
│   ├── subject_menu.py
│   └── utils.py
│
├── docs/
│   └── testing/
│       ├── bug_reports/
│       │   ├── BR_001.md
│       │   ├── BR_002.md
│       │   ├── BR_003.md
│       │   └── BR_004.md
│       │
│       ├── test_runs/
│       │   └── test_run_01.md
│       │
│       │
│       ├── test_summary/
│       │   └── test_summary_report_01.md
│       │
│       │
│       ├── checklist.md
│       └── test_plan.md
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Тестирование

Для приложения проведено функциональное тестирование.

Подготовлены следующие артефакты:

- Test Plan
- Checklist (48 сценариев)
- Test Run (результаты тестирования)
- Bug Reports (4 дефекта)
- Test Summary Reports (Итоговая оценка приложения)

Подробности в папке docs/testing/

---

## Планы по развитию

- добавление статистики
- расширенная аналитика по предметам
- улучшение интерфейса

---

## Лицензия

Проект распространяется как открытое программное обеспечение.
