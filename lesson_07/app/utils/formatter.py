"""Форматирование денежных сумм и заголовков."""

def format_kopeks(kopeks: int) -> str:
    """Преобразует сумму в копейках в строку с рублями.

    Args:
        kopeks: Сумма в копейках.

    Returns:
        Сумма в формате «1 250,00 ₽».
    """
    return f"{kopeks / 100:,.2f} ₽".replace(",", " ").replace(".", ",")


def format_title(text: str, width: int = 40) -> str:
    """Центрирует заголовок и заполняет строку знаками равенства.

    Args:
        text: Текст заголовка.
        width: Итоговая ширина строки.

    Returns:
        Отформатированный заголовок.
    """
    return text.center(width, "=")
