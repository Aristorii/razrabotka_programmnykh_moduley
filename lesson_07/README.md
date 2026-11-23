# Отчёт кафе — занятие 7: докстринги и Ruff

## Запуск

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

## Проверки

```bash
python -m pytest -v
ruff check app
mypy app
```

## Что сделано

- Добавлены Google-style docstrings к публичным модулям, классам и функциям.
- Для Ruff включены правила `E`, `F` и `D`, стиль докстрингов — Google.
- Для autoDocstring подготовлены настройки VS Code с форматом `google-notypes`.
- Добавлен сниппет `dsg` для вставки шаблона Google docstring.
- Вариантный модуль `app/services/report_file.py` оформлен и проходит Ruff без замечаний.


