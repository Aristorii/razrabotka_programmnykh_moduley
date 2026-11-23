"""Форматирование текущей даты."""

from datetime import date


def today_label() -> str:
    """Возвращает сегодняшнюю дату в формате ДД.ММ.ГГГГ.

    Returns:
        Строка с текущей датой.
    """
    return date.today().strftime("%d.%m.%Y")
