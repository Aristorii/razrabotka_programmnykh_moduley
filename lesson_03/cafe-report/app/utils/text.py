def clean_text(value: str) -> str:
    """Убирает лишние пробелы из строки."""
    return " ".join(value.split())
