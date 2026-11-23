def format_money(value: float) -> str:
    """Форматирует сумму в рублях с двумя знаками после запятой."""
    whole, fraction = f"{value:,.2f}".split(".")
    return f"{whole.replace(',', ' ')},{fraction} ₽"
