# Отчёт о расходах в поездке

from rich import print
from calculator import calculate_total, calculate_average


expenses = [
    1200,
    850,
    600,
    1500,
    450,
    700,
    900,
    500,
    800,
    400,
]


def format_report():
    """Формирует и выводит отчёт о расходах."""
    total = calculate_total(expenses)
    average = calculate_average(expenses)

    report = [
        "[bold green]ОТЧЁТ ПО ПОЕЗДКЕ[/bold green]",
        "--------------------------------",
        f"записей: {len(expenses)}",
        f"всего потрачено: {total} ₽",
        f"средняя трата: {average:.2f} ₽",
    ]

    print("\n".join(report))


if __name__ == "__main__":
    format_report()
