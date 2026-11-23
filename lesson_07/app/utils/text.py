"""Обработка текстовых значений."""

def _squash_spaces(value: str) -> str:
    """Заменяет последовательности пробелов одним пробелом.

    Args:
        value: Исходная строка.

    Returns:
        Строка с нормализованными пробелами.
    """
    return " ".join(value.split())


def normalize_name(name: str) -> str:
    """Нормализует имя: убирает лишние пробелы и делает заглавные буквы.

    Args:
        name: Имя или ФИО в произвольном регистре.

    Returns:
        Нормализованное имя.
    """
    return _squash_spaces(name).title()
