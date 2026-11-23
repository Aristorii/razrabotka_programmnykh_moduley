# Отчёт кафе — занятие 7: докстринги и Ruff

Готовый учебный проект по теме «Докстринги в VS Code: генератор и проверка».
Вариант модуля: `app/services/report_file.py`.

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

## Перед сдачей

1. Открой проект в VS Code.
2. Установи расширения **autoDocstring** (`njpwerner.autodocstring`) и **Ruff** (`charliermarsh.ruff`).
3. Выполни команды проверок из раздела выше и сделай собственные скриншоты.
4. Заполни данные студента и вставь свои скриншоты в `img/`.
5. Проверь, что можешь объяснить назначение докстрингов и замечания Ruff.

Скриншоты из чужого отчёта не включены: их нужно сделать в своей среде.
