# Cafe Report

Программа читает заказы из `data/orders.csv` и выводит отчёт по количеству заказов, общей выручке и среднему чеку.

## Запуск

Из папки `cafe-report`:

```bash
python -m app.main
python -m unittest discover -s tests -v
```

## Структура

- `app/main.py` — точка входа
- `app/services/` — загрузка заказов и формирование отчёта
- `app/utils/` — форматирование денег и текста
- `data/` — исходные данные CSV
- `docs/` — документация
- `tests/` — тесты
