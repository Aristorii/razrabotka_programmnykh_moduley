"""Вспомогательные функции для расчётов."""

def calculate_average(grades: list[int]) -> float:
    """Вычисляет среднее арифметическое оценок.

    Args:
        grades: Список целочисленных оценок.

    Returns:
        Среднее значение, округлённое до двух знаков.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not grades:
        raise ValueError("Список оценок пуст")
    return round(sum(grades) / len(grades), 2)


def grade_bounds(grades: list[int]) -> tuple[int, int]:
    """Находит минимальную и максимальную оценки.

    Args:
        grades: Список целочисленных оценок.

    Returns:
        Кортеж из минимальной и максимальной оценок.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not grades:
        raise ValueError("Список оценок пуст")
    return min(grades), max(grades)
