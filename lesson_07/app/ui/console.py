"""Вывод отчёта в консоль."""

def print_report(lines: list[str]) -> None:
    """Печатает строки отчёта по одной на строку.

    Args:
        lines: Строки готового отчёта.
    """
    for line in lines:
        print(line)
