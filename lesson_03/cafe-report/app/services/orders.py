import csv
from pathlib import Path


def load_orders(path: str | Path) -> list[dict[str, str]]:
    """Загружает заказы из CSV-файла."""
    with open(path, encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def order_total(order: dict[str, str]) -> float:
    return int(order["quantity"]) * float(order["price"])


def calculate_revenue(orders: list[dict[str, str]]) -> float:
    return sum(order_total(order) for order in orders)
